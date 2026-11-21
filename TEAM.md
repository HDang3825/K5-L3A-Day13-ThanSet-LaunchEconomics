# Team

## Thông tin nhóm

- Tên nhóm: ThanSet
- Lớp: L3A
- Nhóm trưởng: Võ Lê Hải Đăng
- Repo nhóm: `K5-L3A-Day13-ThanSet-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/HDang3825/K5-L3A-Day13-ThanSet-LaunchEconomics (đang làm việc trên các nhánh thành viên, sẽ chốt nhánh `main` trước khi nộp) · commit chốt: (điền lúc 17:45)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Võ Lê Hải Đăng (nhóm trưởng) | 2A202603577 | 26ai.dangvlh@vinuni.edu.vn | HDang3825 | Kỹ sư Dữ liệu 1 (người viết code nửa đầu buổi) |
|   2 | Lưu Đăng Tuấn | 2A202603454 | 26ai.tuanld@vinuni.edu.vn | kegacua | Kỹ sư Dữ liệu 2 / Kiểm toán số liệu (người kiểm số; người viết code nửa sau buổi) |
|   3 | Nguyễn Thành Danh | 2A202603493 | 26ai.danhnt@vinuni.edu.vn |  thdanhnguyen | Chuyên viên Đảm bảo chất lượng (QA, người gắn nhãn 1) |
|   4 | Nguyễn Thị Hồng San | 2A202603513 | 26ai.sannth@vinuni.edu.vn | nghongsan | Quản lý Hồ sơ & Vận hành (người gắn nhãn 2 kiêm giữ hồ sơ) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## VoLeHaiDang-2A202603577

### Phần việc phụ trách

- Lập trình mô hình kinh tế và phân tích độ nhạy trong `src/lab13.py` (CP1 và CP2).
- Hoàn thiện bảng dữ liệu chi phí và độ nhạy trong `report/team/bang_chi_phi.md`.
- Thiết kế đặc tả 8 Telemetry Events có `trace_id` và phân tích định lượng 3 rủi ro kinh tế trong `report/team/chi_so.md` (CP5).
- Đồng hoàn thiện Hồ sơ Launch v0 (`report/team/ho_so_launch_v0.md`).

### Đóng góp cụ thể

- Lập trình 3 hàm A1 kinh tế chạy lại, vượt qua 100% ba phép thử biết trước (1,20 · 1,25 · 1,25).
- Xây dựng hàm `mo_hinh` A2 tính toán chi phí mỗi việc thành công (4.472 đ [simulated], gấp 16,3 lần hóa đơn token + tool), phát hiện chi phí nhân viên chiếm 92,5% tổng chi phí.
- Phân tích chi phí 4 loại yêu cầu (A3), chỉ ra loại `quoc_te` không đáng chạy (22.515 đ, thành công chỉ 27,3%) và tỉ lệ thành công giảm nhanh theo lượt chạy.
- Tính chi phí cố định 40tr/tháng cho phạm vi `noi_dia + hang_nang` (A4): 4.599 đ (0,38× so với 12.000 đ).
- Mô phỏng 9 kịch bản độ nhạy (B1), kịch bản cặp (B2), phân tích tối ưu toàn cục của giới hạn 2 lần chạy (B3: 6.901.220 đ) và rủi ro chi phí khi xem lại 100% (B4: vọt lên 1,04× baseline).
- Xây dựng đặc tả 8 telemetry events có `trace_id` và 3 rủi ro kinh tế trong `chi_so.md`; hoàn thiện 7 mục và 3 điều kiện duyệt Go có điều kiện trong `ho_so_launch_v0.md`.

### Bằng chứng

- Nhánh `dang`: commits trên `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
- Báo cáo cá nhân: `report/team/2A202603577_VoLeHaiDang.md`.

## LuuDangTuan-2A202603454

### Phần việc phụ trách

- Kiểm toán số liệu CP1 & CP2 (tính tay kiểm chéo với code của Thành viên 1, rà soát và chuẩn hoá `report/team/bang_chi_phi.md`).
- Viết code phần CP4 (Nhiệm vụ D: tính cỡ mẫu, hệ số thiết kế cụm ICC = 0,02, power đánh đổi, tỉ lệ mở lại 7 ngày) trong `src/lab13.py`.
- Điền kết quả D1, D2, đánh đổi và các tham số định lượng trong `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Tính tay kiểm chéo A1–A4 và B1–B4 trực tiếp từ `logix_runs.csv` và `logix_requests.csv`; phát hiện và sửa lỗi nhận định biến động giá token ở B2 (`+5,6% / −2,8%`), sửa làm tròn A2 (`93.804 đ`), bổ sung hai mốc phút làm lại thực tế ở B4 (`15,3` và `16,25` phút), chuẩn hoá nhãn `simulated` trên toàn bộ `report/team/bang_chi_phi.md`.
- Viết hàm `co_mau_hai_ti_le()` và `chay_nhiem_vu_d()` trong `src/lab13.py`, đối chiếu công thức chuẩn z với `statsmodels` (`1.251` vs `1.250`), tính đủ 5 câu D1, power đánh đổi (`0,64`) và tỉ lệ `mo_lai_trong_7_ngay` (`4,25%` toàn mẫu, `3,97%` phạm vi).
- Điền chú thích D1–D2 và thông số `assignment`/`primary_metric` trong `report/team/pilot_plan.yaml`, kiểm tra hợp lệ bằng `yaml.safe_load`.

### Bằng chứng

- Nhánh `luutuan`, commit `9736e52` trên `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`.
- Báo cáo cá nhân: `report/team/2A202603454_LuuDangTuan.md`.

## NguyenThanhDanh-2A202603493

### Phần việc phụ trách

- Đóng vai trò "Người gác cổng", theo dõi điều kiện "Xong khi" của từng checkpoint trong `CHECKPOINTS.md` và tiêu chí chấm trong `RUBRIC.md` (kiểm soát nhãn `simulated`, không dùng từ `"production"`, người phụ trách là vai trò cụ thể).
- Gắn nhãn độc lập 20 ca lỗi theo 5 nhóm của Google PAIR, đối chiếu với Người gắn nhãn 2 để tính tỉ lệ đồng thuận, viết quy tắc phân biệt cho các ca không trùng và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Chủ trì hoàn thiện cấu trúc `report/team/pilot_plan.yaml`, thiết lập 3 luật dừng định lượng theo mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`, xác định `identifiability`, `rollback`, `scope`, `simulated_inputs` và kiểm tra cú pháp YAML.

### Đóng góp cụ thể

- Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gắn nhãn độc lập toàn bộ 20 ca theo nguyên nhân gốc (4 ca *Do người dùng*, 5 ca *Hệ thống*, 4 ca *Ngữ cảnh*, 4 ca *Giới hạn hệ thống*, 3 ca *Ngầm*).
- Gộp bảng nhãn độc lập với Người gắn nhãn 2 (Nguyễn Thị Hồng San), đạt tỉ lệ đồng thuận **17/20 = 85%** (vượt ngưỡng $\ge 80\%$).
- Soạn 3 câu quy tắc phân biệt cho 3 ca lệch (Ca 13, Ca 16, Ca 17) và hoàn thiện bảng khắc phục 5 ca đại diện đủ 5 loại lỗi (Ca 9, Ca 7, Ca 18, Ca 4, Ca 17) với cách phát hiện đo được (event, ngưỡng, tần suất) và vai trò phụ trách cụ thể.
- Hoàn thiện các trường định tính, phạm vi (`noi_dia` + `hang_nang`), danh sách `simulated_inputs` và 3 luật dừng (an toàn, chi phí, mức độ sử dụng) trong `report/team/pilot_plan.yaml`.

### Bằng chứng

- `report/team/bang_loi.md`: Đủ 20 ca đối chiếu (tỉ lệ đồng thuận `17 / 20 = 85%`), 3 quy tắc phân biệt (Ca 13, 16, 17) và 5 dòng khắc phục đủ 5 nhóm PAIR.
- `report/team/pilot_plan.yaml`: Đọc thành công bằng `yaml.safe_load` (`YAML valid: True`), không còn dấu `?` ngoài dòng chú thích, đủ 3 luật dừng đúng mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- Nhánh cá nhân: `nguyenthanhdanh` .
- Báo cáo cá nhân `report/team/2A202603493_NguyenThanhDanh.md` .

## NguyenThiHongSan-2A202603513

### Phần việc phụ trách

- Người giữ hồ sơ: theo dõi `report/team/ho_so_launch_v0.md` từ đầu buổi, rà soát tính nhất quán (nhãn `simulated`, chức danh người phụ trách, không còn chỗ trống, từ cấm).
- Người gắn nhãn 2 ở CP3: gắn độc lập 20 ca lỗi theo 5 loại Google PAIR trong `report/team/bang_loi.md`.
- Điền thông tin nhóm và bảng thành viên trong `TEAM.md`; chuẩn bị chấm duyệt chéo Gate 2a bằng `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi (bộ nhãn người 2); đồng thuận với người gắn nhãn 1 là 17/20 = 85%.
- Rà soát hồ sơ launch v0 với số trong `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`; tính tay kiểm số 3.414 đ (phạm vi `noi_dia` + `hang_nang`, simulated): (2.696 × 783 + 8.221 × 117) ÷ 900 = 3.414 đ, khớp hồ sơ.
- Điền bảng thành viên, vai và thông tin nhóm trong `TEAM.md`; kéo `main` về nhánh `nghongsan` và gộp xung đột ở `TEAM.md`, `ho_so_launch_v0.md`.

### Bằng chứng

- Nhánh `nghongsan`, commit `94734dc` (`report/team/bang_loi.md`) và `3b5f8b0` (`TEAM.md`, báo cáo cá nhân).
- Báo cáo cá nhân: `report/team/2A202603513_NguyenThiHongSan.md`.
