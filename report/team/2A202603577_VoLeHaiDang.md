# Báo cáo cá nhân — Võ Lê Hải Đăng · 2A202603577

## 1. Thông tin thành viên

- Họ tên: Võ Lê Hải Đăng
- MSSV: 2A202603577
- Email: 26ai.dangvlh@vinuni.edu.vn
- GitHub: HDang3825
- Vai trong nhóm: **Người viết code (Kỹ sư Dữ liệu 1)** nửa đầu buổi (CP1, CP2); **Chuyên viên Kỹ thuật & Rủi ro kinh tế** nửa sau buổi (CP5).

## 2. Phần việc phụ trách

- Chịu trách nhiệm chính việc lập trình mô hình kinh tế và phân tích độ nhạy trong file `src/lab13.py` (Nhiệm vụ A và B).
- Hoàn thiện bảng dữ liệu chi phí thực tế và kiểm tra độ nhạy trong file `report/team/bang_chi_phi.md`.
- Chịu trách nhiệm thiết kế đặc tả 8 Telemetry Events có `trace_id` và phân tích định lượng 3 rủi ro kinh tế trong file `report/team/chi_so.md`.
- Tham gia tổng hợp và rà soát các điều kiện nghiệm thu trong Hồ sơ Launch v0 (`report/team/ho_so_launch_v0.md`).

## 3. Đóng góp cụ thể

1. **Nhiệm vụ A1 (Kinh tế của việc chạy lại):**
   - Lập trình 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` trong `src/lab13.py`.
   - Vượt qua 100% ba phép thử kiểm tra tự động biết trước ($1,20 \cdot 1,25 \cdot 1,25$).
2. **Nhiệm vụ A2 (Mô hình chi phí từ trace):**
   - Viết hàm `mo_hinh(runs, reqs, ...)` xử lý trace logs và requests.
   - Tính toán chính xác chi phí mỗi việc thành công là **4.472 đ** [simulated], gấp **16,3 lần** hóa đơn token + tool (274,7 đ).
   - Chỉ ra giờ làm việc của nhân viên chiếm tỷ trọng áp đảo **92,5%** [simulated] tổng chi phí (làm lại 51,8%, xem lại 40,7%).
3. **Nhiệm vụ A3 & A4 (Phân rã theo loại & Chi phí cố định):**
   - Phân tích chi phí theo 4 loại: chứng minh loại `quoc_te` không hiệu quả kinh tế (chi phí 22.515 đ = 1,88× nhân viên tự làm, thành công chỉ 27,3%) và tỷ lệ thành công giảm dần theo từng lần chạy lại (30% $\rightarrow$ 11,4% $\rightarrow$ 2,2%). Đề xuất loại bỏ khỏi phạm vi pilot.
   - Tính toán chi phí cố định 40 triệu/tháng: với phạm vi `noi_dia + hang_nang` ở quy mô 45.000 YC/tháng, chi phí gồm cố định là **4.599 đ** (0,38× so với 12.000 đ) [simulated].
4. **Nhiệm vụ B (Bảng độ nhạy B1–B4):**
   - Lập trình 9 kịch bản độ nhạy (B1), kịch bản cặp (B2), xếp hạng 3 yếu tố nhạy nhất: 1. Số ca làm lại (+51,8%), 2. Tỉ lệ xem lại (+40,7%), 3. Lương nhân viên (+23,1%). Chứng minh giá token ít nhạy nhất (±5,6%).
   - Phân tích giới hạn số lần chạy (B3): phát hiện mâu thuẫn giữa tối ưu cục bộ và toàn cục — giới hạn 1 lần chạy cho CPS agent thấp nhất (4.111 đ) nhưng **giới hạn 2 lần chạy mới rẻ nhất cho toàn công ty (6.901.220 đ)** vì tránh đẩy 85 việc sang nhân viên.
   - Phân tích xem lại 100% (B4): tính toán chứng minh nếu bắt xem lại 100%, chi phí tăng lên **11.743 đ – 12.516 đ** ($0,98\times – 1,04\times$ nhân viên tự làm) [simulated], triệt tiêu hoàn toàn hiệu quả của AI.
5. **Nhiệm vụ E (Telemetry Events & Rủi ro kinh tế):**
   - Xây dựng danh sách 8 Telemetry Events bắt buộc mang `trace_id` trong `chi_so.md`, thiết lập bảng kiểm tra chéo liên kết giữa event và công thức tính chỉ số.
   - Định lượng 3 rủi ro kinh tế lớn kèm ngưỡng cảnh báo và kế hoạch hành động.
   - Đồng hoàn thiện `ho_so_launch_v0.md` với đề xuất "Go có điều kiện" và 3 điều kiện định lượng cụ thể.

## 4. Bằng chứng

- **Mã nguồn code:** Hàm A1, hàm `mo_hinh`, bảng B1–B4 trong file [src/lab13.py](file:///c:/Hdang/VinUni/K5-L3A-Day13-ThanSet-LaunchEconomics/src/lab13.py), chạy kiểm thử qua `..\venv\Scripts\python.exe lab13.py` đạt chuẩn sai số 0%.
- **Bảng số liệu & Hồ sơ:**
  - [report/team/bang_chi_phi.md](file:///c:/Hdang/VinUni/K5-L3A-Day13-ThanSet-LaunchEconomics/report/team/bang_chi_phi.md): Hoàn thành toàn bộ bảng A1, A2, A3, A4, B1, B2, B3, B4.
  - [report/team/chi_so.md](file:///c:/Hdang/VinUni/K5-L3A-Day13-ThanSet-LaunchEconomics/report/team/chi_so.md): Đặc tả 8 events và 3 rủi ro kinh tế.
  - [report/team/ho_so_launch_v0.md](file:///c:/Hdang/VinUni/K5-L3A-Day13-ThanSet-LaunchEconomics/report/team/ho_so_launch_v0.md): Hồ sơ 1 trang chốt Gate 2a.
- **Git commits:**
  - Commit: `Hoan thanh CP1 va CP2: mo hinh chi phi va bang do nhay`
  - Commit: `Hoan thanh CP5: dac ta chi so, telemetry events va ho so launch v0`

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini 3.8.
- **Mục đích sử dụng:**
  - Hỗ trợ giải thích bản chất kinh tế của việc chạy lại (hiện tượng tỷ lệ thành công giảm dần qua các lần chạy).
  - Gợi ý cấu trúc tính chất cộng tuyến tính trong bảng phân tích độ nhạy.
- **Cách tự kiểm tra và kiểm chứng:**
  - Tự chạy script `python lab13.py` trên môi trường Python local, kiểm tra terminal output.
  - Đối chiếu trực tiếp từng con số tính ra với tài liệu chuẩn `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và slide bài giảng (đảm bảo độ lệch 0%).
  - Dùng script kiểm tra cú pháp YAML `yaml.safe_load` và rà soát tự động không có từ cấm `production` trong hồ sơ.

## 6. Tự đánh giá

- **Mức độ hoàn thành:** 100% nhiệm vụ được giao, hoàn thành trước hạn và đạt chất lượng cao.
- **Điểm tự đánh giá:** 10 / 10.
