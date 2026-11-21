# Báo cáo cá nhân — NguyenThanhDanh-2A202603493

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thành Danh
- MSSV: 2A202603493
- Email: (điền email của bạn) 26ai.danhnt@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (QA / Người gác cổng)

## 2. Phần việc phụ trách

- **Xuyên suốt buổi (CP1–CP5):** Đóng vai trò "Người gác cổng", theo dõi điều kiện "Xong khi" của từng checkpoint trong `CHECKPOINTS.md` và tiêu chí chấm trong `RUBRIC.md` (kiểm soát nhãn `simulated`, không dùng từ `"production"`, người phụ trách là vai trò cụ thể).
- **Nhiệm vụ C (CP3):** Gắn nhãn độc lập 20 ca lỗi theo 5 nhóm của Google PAIR, đối chiếu với Người gắn nhãn 2 để tính tỉ lệ đồng thuận, viết quy tắc phân biệt cho các ca không trùng và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- **Nhiệm vụ D (CP4):** Chủ trì hoàn thiện cấu trúc `report/team/pilot_plan.yaml`, thiết lập 3 luật dừng định lượng theo mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`, xác định `identifiability`, `rollback`, `scope`, `simulated_inputs` và kiểm tra cú pháp YAML.
- **Nhiệm vụ E (CP5):** Phối hợp kiểm tra chéo và hoàn thiện `report/team/chi_so.md` và trang hồ sơ `report/team/ho_so_launch_v0.md` trước phiên duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gắn nhãn độc lập toàn bộ 20 ca theo nguyên nhân gốc (4 ca *Do người dùng*, 5 ca *Hệ thống*, 4 ca *Ngữ cảnh*, 4 ca *Giới hạn hệ thống*, 3 ca *Ngầm*).
- Gộp bảng nhãn độc lập với Người gắn nhãn 2 (Nguyễn Thị Hồng San), đạt tỉ lệ đồng thuận **17/20 = 85%** (vượt ngưỡng $\ge 80\%$).
- Soạn 3 câu quy tắc phân biệt cho 3 ca lệch (Ca 13, Ca 16, Ca 17) và hoàn thiện bảng khắc phục 5 ca đại diện đủ 5 loại lỗi (Ca 9, Ca 7, Ca 18, Ca 4, Ca 17) với cách phát hiện đo được (event, ngưỡng, tần suất) và vai trò phụ trách cụ thể.
- Hoàn thiện các trường định tính, phạm vi (`noi_dia` + `hang_nang`), danh sách `simulated_inputs` và 3 luật dừng (an toàn, chi phí, mức độ sử dụng) trong `report/team/pilot_plan.yaml`.

## 4. Bằng chứng

- `report/team/bang_loi.md`: Đủ 20 ca đối chiếu (tỉ lệ đồng thuận `17 / 20 = 85%`), 3 quy tắc phân biệt (Ca 13, 16, 17) và 5 dòng khắc phục đủ 5 nhóm PAIR.
- `report/team/pilot_plan.yaml`: Đọc thành công bằng `yaml.safe_load` (`YAML valid: True`), không còn dấu `?` ngoài dòng chú thích, đủ 3 luật dừng đúng mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI Gemini).
- **Mục đích sử dụng:** Rà soát checklist checkpoint/rubric cho vai trò QA, hỗ trợ gộp bảng đối chiếu nhãn từ hai người gắn nhãn, chuẩn hóa cấu trúc `pilot_plan.yaml` và cú pháp luật dừng, kiểm tra tính toán các chỉ số E1 trên `src/logix_requests.csv`.
- **Cách tự kiểm tra:**
  - Đối chiếu trực tiếp nhãn từng ca với 5 định nghĩa Google PAIR trong đề bài và lý do nguyên nhân gốc.
  - Chạy lệnh Python kiểm tra cú pháp YAML (`yaml.safe_load`) và quét toàn bộ file trong `report/team/` để đảm bảo không còn dấu `?` ngoài chú thích và không có từ `"production"`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ vai trò **Người gắn nhãn 1 / QA** đúng tiến độ từng checkpoint, đảm bảo tính độc lập khi gắn nhãn 20 ca lỗi (đạt 85% đồng thuận) và kiểm soát tốt các quy định dễ mất điểm của rubric (`simulated`, không dùng `"production"`, luật dừng có ngưỡng/thời hạn/người có quyền dừng, nêu rõ con số bất lợi `power = 0,64` trong đề xuất).
