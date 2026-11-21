# Báo cáo cá nhân — LuuDangTuan-2A202603454

## 1. Thông tin thành viên

- Họ tên: Lưu Đăng Tuấn
- MSSV: 2A202603454
- Email: 26ai.tuanld@vinuni.edu.vn
- GitHub: `kegacua`
- Vai trong nhóm: **Người kiểm số (nửa đầu buổi)** kiêm **Người viết code (nửa sau buổi)** — Thành viên 2.

## 2. Phần việc phụ trách

- **CP1 & CP2 (Nhiệm vụ A, B — Người kiểm số):** Tính tay kiểm chéo độc lập các công thức và số liệu từ hai file dữ liệu gốc (`src/logix_runs.csv`, `src/logix_requests.csv`) với code của Thành viên 1 (nhánh `dang`, đảm bảo sai lệch ≤ 2%); rà soát và hoàn thiện `report/team/bang_chi_phi.md` (chuẩn hoá nhãn `simulated`, giới hạn độ dài ≤ 3 dòng/câu).
- **CP4 (Nhiệm vụ D — Người viết code):** Viết phần code tính cỡ mẫu, hệ số thiết kế cụm (`ICC = 0,02`), cỡ mẫu hiệu dụng, power đánh đổi và tỉ lệ mở lại 7 ngày trong `src/lab13.py`; điền phần chú thích đầu file (D1, D2, đánh đổi, tỉ lệ mở lại hiện tại) và các tham số định lượng vào `report/team/pilot_plan.yaml`.
- **Gate 2a & Đóng gói:** Chuẩn bị phần bảo vệ số liệu kinh tế – thiết kế mẫu và kiểm thử chạy sạch `src/lab13.py` + `yaml.safe_load` trên môi trường ảo `.venv`.

## 3. Đóng góp cụ thể

- **Kiểm toán CP1 & CP2 (`report/team/bang_chi_phi.md`):**
  - Tính tay kiểm chéo 3 phép thử A1 (`1,20`, `1,25`, `1,25`), tổng các khoản A2 (`token = 245.585 đ`, `tool = 84.000 đ`, `xem_lai = 1.780.000 đ` [simulated], `lam_lai = 2.264.000 đ` [simulated], `CPS = 4.472 đ` [simulated], gấp `16,3 lần` hoá đơn mỗi yêu cầu `274,7 đ`), bảng A3 theo 4 loại yêu cầu, A4 cộng chi phí cố định 40 triệu đ/tháng (`4.599 đ = 0,38×` và `5.784 đ = 0,48×` [simulated]), và bảng độ nhạy B1–B4.
  - Phát hiện và sửa các lỗi chi tiết trong bản đầu: sửa làm tròn `attempt > 1` (`93.804 đ`), sửa nhận định biến động giá token ở B2 (từ `±5,6%` thành `+5,6%` khi gấp đôi và `−2,8%` khi giảm một nửa), bổ sung đầy đủ cả hai mốc phút làm lại thực tế ở B4 (`15,3 phút` TB toàn mẫu → `12.414 đ = 1,03×` và `16,25 phút` TB phạm vi → `12.516 đ = 1,04×`, simulated), chuẩn hoá toàn bộ nhãn `simulated`.
- **Viết code CP4 (`src/lab13.py`):**
  - Cài đặt môi trường ảo `src/.venv` với đầy đủ thư viện trong `src/requirements.txt`.
  - Viết hàm `co_mau_hai_ti_le()` và `chay_nhiem_vu_d()` tính 5 câu D1: (a) `1.251` yc/nhóm (`statsmodels: 1.250`); (b) theo nhân viên `m = 75` có `DE = 2,48`, cần `3.103` yc/nhóm (`42` NV/nhóm, tổng `84 > 40`, không đủ người); (c) `20` NV/nhóm có trần `c/ICC = 1.000 < 1.251`; (d) `6` depot/nhóm có trần `300`; (e) nâng MDE lên `6` điểm (`n = 859/nhóm`) với `20` NV/nhóm cần `m ≥ 299` yc/NV (`DE = 6,96`), kèm power đánh đổi còn `0,64` nếu tác động thật chỉ `+5` điểm.
  - Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` phạm vi `noi_dia + hang_nang`) để Thành viên 3 thiết lập ngưỡng dừng an toàn hợp lý.
- **Điền phần định lượng & chú thích (`report/team/pilot_plan.yaml`):**
  - Hoàn thiện mục chú thích D1, D2 (5 câu tách được tác động), Đánh đổi đã chấp nhận, Tỉ lệ mở lại hiện tại và các trường số của `assignment` & `primary_metric` (`unit: "staff"`, `mde: 0.06`, `n_per_arm: 859`, `design_effect: 6.96`, `clusters_per_arm: 20`).

## 4. Bằng chứng

- Nhánh làm việc riêng: `luutuan` (không làm trực tiếp trên `main`), pull từ nhánh `dang` của Thành viên 1.
- Commit chốt phần kỹ thuật CP1–CP2–CP4: `9736e52` — *"TV2: audit CP1-CP2 bang_chi_phi.md, add CP4 sample size code and D1-D2 in pilot_plan.yaml"*.
- Các file đã chỉnh sửa/đóng góp:
  - `src/lab13.py`: chạy từ đầu đến cuối thoát mã `0`, ba phép thử A1 in `ĐẠT`, in đủ A1–A4, B1–B4, D1.
  - `report/team/bang_chi_phi.md`: đầy đủ bảng A1–B4, mọi số giả lập có nhãn `simulated`, không có từ bị cấm.
  - `report/team/pilot_plan.yaml`: đã điền D1, D2, `assignment`, `primary_metric`; kiểm tra đọc hợp lệ bằng `yaml.safe_load`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI lập trình tích hợp trong IDE).
- **Mục đích sử dụng:** Giải thích nhanh yêu cầu và tiêu chí rubric của Lab 13, hỗ trợ kiểm tra đối chiếu công thức tính tay CP1–CP2, gợi ý cấu trúc hàm tính cỡ mẫu CP4 (`NormalDist` kết hợp `statsmodels`) và soát lỗi định dạng/nhãn `simulated` trong báo cáo.
- **Cách tự kiểm tra kết quả:**
  - Tự đối chiếu các phép tính tay từ tổng số liệu thô (`tokens_in`, `tokens_out`, `tool_calls`, phút xem lại/làm lại, số ca thành công) so với output của `src/lab13.py` (sai lệch = 0%) và đối chiếu với mốc tự kiểm của tài liệu hướng dẫn.
  - Kiểm tra tính tuyến tính của bảng độ nhạy B1–B2 (mức giảm khi chia đôi bằng đúng nửa mức tăng khi gấp đôi; đổi cặp B2 bằng tổng hai mức riêng).
  - Kiểm tra chéo công thức cỡ mẫu viết tay (`NormalDist`) với thư viện `statsmodels.stats.power.NormalIndPower` (`1.251` vs `1.250`, lệch < 0,1%) và xác thực file YAML bằng `yaml.safe_load`.

## 6. Tự đánh giá

- **Điểm làm tốt:** Hoàn thành đúng vai trò kiểm toán số liệu (phát hiện và sửa lỗi nhận định B2, làm tròn A2, chuẩn hoá nhãn `simulated`) và triển khai gọn, đầy đủ phần code tính cỡ mẫu cụm CP4 cùng phần chú thích D1–D2 trong `pilot_plan.yaml`, giúp Thành viên 3 có đủ nền tảng số để chốt luật dừng.
- **Điểm cần lưu ý / cải thiện:** Cần phối hợp chặt với Thành viên 3 và Thành viên 4 sau khi ghép nhánh để rà soát toàn bộ `pilot_plan.yaml` không còn dấu `?` và đảm bảo các con số trên `ho_so_launch_v0.md` đồng bộ 100% với `bang_chi_phi.md` và `pilot_plan.yaml`.
