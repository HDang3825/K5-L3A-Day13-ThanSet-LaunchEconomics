"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong > 0 else 0,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) > 0 else 0,
    )


# ---------- Nhiệm vụ D · Cỡ mẫu và thiết kế pilot (CP4) ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức chuẩn z)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    n = (
        za * math.sqrt(2 * p_bar * (1 - p_bar))
        + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def chay_nhiem_vu_d(reqs, p1=0.70, mde_goc=0.05, mde_moi=0.06, alpha=0.05, power=0.80, icc=0.02):
    """Tính 5 câu D1, power đánh đổi khi nâng MDE lên 6 điểm, và tỉ lệ mở lại 7 ngày hiện tại."""
    print('\n=== D1 · Cỡ mẫu theo ba cách chia (CP4) ===')
    n_req_5 = co_mau_hai_ti_le(p1, p1 + mde_goc, alpha=alpha, power=power)
    es_5 = proportion_effectsize(p1 + mde_goc, p1)
    n_sm_5 = math.ceil(NormalIndPower().solve_power(effect_size=es_5, alpha=alpha, power=power, ratio=1.0))

    m_b = 75
    de_b = 1 + (m_b - 1) * icc
    n_b = math.ceil(n_req_5 * de_b)
    nv_moi_nhom = math.ceil(n_b / m_b)

    c_nv = 20
    tran_nv = c_nv / icc
    c_depot = 6
    tran_depot = c_depot / icc

    n_req_6 = co_mau_hai_ti_le(p1, p1 + mde_moi, alpha=alpha, power=power)
    m_min = math.ceil(((1 - icc) * n_req_6) / (c_nv - icc * n_req_6))
    de_e = 1 + (m_min - 1) * icc
    n_eff_e = (c_nv * m_min) / de_e
    power_5 = NormalIndPower().power(effect_size=es_5, nobs1=n_req_6, alpha=alpha, ratio=1.0)

    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    reopen_all = reqs['mo_lai_trong_7_ngay'].mean()
    reopen_scope = scope['mo_lai_trong_7_ngay'].mean()

    print(f"a) Chia theo yêu cầu (+5 điểm):         {n_req_5:,} yêu cầu/nhóm (statsmodels: {n_sm_5:,})")
    print(f"b) Theo nhân viên (m=75):               DE={de_b:.2f}, n={n_b:,}/nhóm -> {nv_moi_nhom} NV/nhóm (tổng {2*nv_moi_nhom} > 40: không đủ người)")
    print(f"c) 20 nhân viên/nhóm:                   n_hiệu_dụng < {tran_nv:,.0f} < {n_req_5:,} (không đạt +5 điểm)")
    print(f"d) 6 depot/nhóm:                        n_hiệu_dụng < {tran_depot:,.0f} (và 6 < 20 cụm/nhóm: loại)")
    print(f"e) Mức chênh 6 điểm (n={n_req_6:,}/nhóm):     m >= {m_min} yc/NV (DE={de_e:.2f}, n_hiệu_dụng={n_eff_e:.1f})")
    print(f"Đánh đổi: với n={n_req_6:,}, power thực tế khi tác động thật là +5 điểm = {power_5:.2f}")
    print(f"Tỉ lệ mo_lai_trong_7_ngay: toàn mẫu = {reopen_all*100:.2f}% ({int(reqs['mo_lai_trong_7_ngay'].sum())}/{len(reqs)}), "
          f"phạm vi noi_dia + hang_nang = {reopen_scope*100:.2f}% ({int(scope['mo_lai_trong_7_ngay'].sum())}/{len(scope)})")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    
    print('=== A1 · Ba phép thử ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'1. p=0.8, toi da 2 lan: {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'2. p=0.8, chay den khi dung: {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'3. p=0.8, toi da 3 lan (he so cps): {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')

    boi_so = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    pct_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    pct_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    pct_nhan_vien = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100
    print(f"\nChi phí mỗi việc thành công gấp: {boi_so:.1f} lần hoá đơn chia số yêu cầu.")
    print(f"Khoản lớn nhất là làm lại: {pct_lam_lai:.1f}% [simulated], tiếp theo là xem lại: {pct_xem_lai:.1f}% [simulated].")
    print(f"Giờ nhân viên chiếm: {pct_nhan_vien:.1f}% [simulated] tổng chi phí.")

    print('\nA3.Tách theo loại yêu cầu')
    loai_list = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    for loai in loai_list:
        sub_reqs = reqs[reqs['loai'] == loai]
        sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        sub_res = mo_hinh(sub_runs, sub_reqs)
        so_yc = len(sub_reqs)
        ti_le_tc = (sub_reqs['ket_qua'] == 'thanh_cong').mean() * 100
        lan_chay_yc = len(sub_runs) / so_yc
        cps = sub_res['cps']
        so_voi_12k = cps / BASELINE
        print(f"{loai:10s} | YC: {so_yc:3d} | TC: {ti_le_tc:5.1f}% | Runs/YC: {lan_chay_yc:.2f} | CPS: {cps:7,.0f} đ [sim] | So với 12k: {so_voi_12k:.2f}x")

    print('\nTỉ lệ OK theo từng lần chạy (attempt) cho từng loại')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    pivot = merged.pivot_table(index='loai', columns='attempt', values='status', aggfunc=lambda s: (s == 'ok').mean() * 100)
    print(pivot.round(1))

    print('\nA4.Chi phí cố định (phạm vi noi_dia + hang_nang)')
    pham_vi_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pham_vi_runs = runs[runs['request_id'].isin(pham_vi_reqs['request_id'])]
    res_pv = mo_hinh(pham_vi_runs, pham_vi_reqs)
    tc_mau = res_pv['thanh_cong']  # 900
    
    # 45.000 yêu cầu / tháng
    tc_thang_full = 45000 * tc_mau / len(reqs)  # 33.750
    cp_cd_viec_full = 40000000 / tc_thang_full  # 1.185 đ
    cps_full = res_pv['cps'] + cp_cd_viec_full
    
    # Một nửa khối lượng (22.500 yêu cầu / tháng)
    tc_thang_half = 22500 * tc_mau / len(reqs)  # 16.875
    cp_cd_viec_half = 40000000 / tc_thang_half  # 2.370 đ
    cps_half = res_pv['cps'] + cp_cd_viec_half
    
    print(f"Toàn bộ (45k YC/tháng): TC={tc_thang_full:,.0f} | Cố định/việc={cp_cd_viec_full:,.0f} đ | CPS+Cố định={cps_full:,.0f} đ [sim] ({cps_full/BASELINE:.2f}x)")
    print(f"Một nửa (22.5k YC/tháng): TC={tc_thang_half:,.0f} | Cố định/việc={cp_cd_viec_half:,.0f} đ | CPS+Cố định={cps_half:,.0f} đ [sim] ({cps_half/BASELINE:.2f}x)")

    print('\nB1. Bảng độ nhạy (9 kịch bản)')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        res = mo_hinh(runs, reqs, **kw)
        cps = res['cps']
        diff_pct = (cps / goc - 1) * 100
        print(f"{ten:27s} | CPS: {cps:7,.0f} đ [sim] | Thay đổi: {diff_pct:+6.1f}%")

    print('\nB2. Đổi một cặp và xếp hạng ')
    res_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    diff_cap_pct = (res_cap['cps'] / goc - 1) * 100
    print(f"Giá token gấp đôi + Xem lại gấp đôi: CPS = {res_cap['cps']:,.0f} đ [sim] ({diff_cap_pct:+6.1f}%)")
    print("Xếp hạng 3 yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51.8%) · 2. Tỉ lệ xem lại (+40.7%) · 3. Lương nhân viên (+23.1%)")

    print('\nB3. Giới hạn chạy lại có thật sự rẻ hơn')
    for k in [1, 2, 3]:
        kw = dict(max_lan_chay=k) if k < 3 else dict()
        res_k = mo_hinh(runs, reqs, **kw)
        tong_tro_ly = res_k['tong']
        tc = res_k['thanh_cong']
        khong_tc = len(reqs) - tc
        ca_he_thong = tong_tro_ly + khong_tc * BASELINE
        cps_k = res_k['cps']
        print(f"Giới hạn {k} lần: Tổng trợ lý = {tong_tro_ly:9,.0f} đ | Không TC = {khong_tc:3d} | Cả hệ thống = {ca_he_thong:9,.0f} đ | CPS = {cps_k:7,.0f} đ [sim]")

    print('\nB4. Nếu phải xem lại tất cả (100%)')
    pv_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pv_runs = runs[runs['request_id'].isin(pv_reqs['request_id'])]
    ok_req_ids = pv_runs[pv_runs['status'] == 'ok']['request_id'].unique()
    so_yc_xem_lai = len(ok_req_ids)
    tien_xem_lai_100 = so_yc_xem_lai * 5 * LUONG_PHUT
    ca_lam_lai = (pv_reqs['ket_qua'] == 'lam_lai').sum()
    tien_lam_lai_9m = ca_lam_lai * 9 * LUONG_PHUT
    phut_lam_lai_tb_toan_mau = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tien_lam_lai_toan_mau = ca_lam_lai * phut_lam_lai_tb_toan_mau * LUONG_PHUT
    phut_lam_lai_tb = pv_reqs.loc[pv_reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tien_lam_lai_thuc = ca_lam_lai * phut_lam_lai_tb * LUONG_PHUT
    tien_token_tool = (pv_runs['tokens_in'] / 1000 * GIA_VAO + pv_runs['tokens_out'] / 1000 * GIA_RA + pv_runs['tool_calls'] * GIA_TOOL).sum()
    tc_pv = (pv_reqs['ket_qua'] == 'thanh_cong').sum()
    tong_9m = tien_token_tool + tien_xem_lai_100 + tien_lam_lai_9m
    cps_9m = tong_9m / tc_pv
    tong_toan_mau = tien_token_tool + tien_xem_lai_100 + tien_lam_lai_toan_mau
    cps_toan_mau = tong_toan_mau / tc_pv
    tong_thuc = tien_token_tool + tien_xem_lai_100 + tien_lam_lai_thuc
    cps_thuc = tong_thuc / tc_pv
    print(f"Xem lại 100% (9 phút làm lại theo đề): Tổng = {tong_9m:,.0f} đ | CPS = {cps_9m:,.0f} đ [simulated] ({cps_9m/BASELINE:.2f}x)")
    print(f"Xem lại 100% ({phut_lam_lai_tb_toan_mau:.1f} phút TB toàn mẫu): Tổng = {tong_toan_mau:,.0f} đ | CPS = {cps_toan_mau:,.0f} đ [simulated] ({cps_toan_mau/BASELINE:.2f}x)")
    print(f"Xem lại 100% ({phut_lam_lai_tb:.2f} phút TB phạm vi): Tổng = {tong_thuc:,.0f} đ | CPS = {cps_thuc:,.0f} đ [simulated] ({cps_thuc/BASELINE:.2f}x)")

    # CP4 · Nhiệm vụ D: cỡ mẫu, hệ số thiết kế, tỉ lệ mở lại 7 ngày
    chay_nhiem_vu_d(reqs)


