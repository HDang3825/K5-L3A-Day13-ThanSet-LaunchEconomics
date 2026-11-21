# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200 yêu cầu) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177 yêu cầu được xem lại) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200 yêu cầu) |
| Dùng (tự đề xuất) | Tỉ lệ áp dụng gợi ý của trợ lý trong nhóm can thiệp | Số yêu cầu nhân viên giữ nguyên gợi ý (`quyet_dinh_xem_lai == 'giu'`) ÷ tổng yêu cầu xử lý | Đo trong pilot (ngưỡng kỳ vọng ≥ 70%) |
| An toàn (tự đề xuất) | Tỉ lệ hoàn tiền sai lệch số tiền qua kiểm tra mẫu độc lập | Số đơn sai lệch số tiền ÷ tổng số đơn kiểm tra mẫu ngẫu nhiên (100 đơn/tuần) | Đo trong pilot (ngưỡng cảnh báo > 1%, bắt lỗi ngầm ca 5, 17) |

*Ghi chú:* Các chỉ số trên ghi nhận "chỉ số trong đợt chạy thử là …", không ghi "trợ lý đã nâng chỉ số": đợt chạy thử chưa có nhóm đối chứng.

## Danh sách event

Hệ thống ghi nhận 8 telemetry events chuẩn, mỗi event bắt buộc có `trace_id` để liên kết chuỗi tác vụ xuyên suốt:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / Hệ thống | `request_id`, `loai`, `so_tien_vnd`, `arm` (control/treatment), `depot`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý AI | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` (ok/loi), `trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (giu/sua/bo), `phut_xem_lai_real`, `trace_id` | Khi nhân viên xác nhận xem lại gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai_real`, `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn thành làm lại đơn sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `status` (ok/fail), `trace_id` | Khi thực hiện lệnh hoàn tiền vào sổ cái |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `dong_trong_24h` (0/1), `trace_id` | Khi yêu cầu được đóng thành công |
| `ticket_reopened` | Khách hàng | `reopened_at`, `mo_lai_trong_7_ngay` (0/1), `ly_do`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |

**Kiểm tra chéo:**
- **Chỉ số chính (% đóng 24h & không mở lại 7 ngày):** Kết hợp thuộc tính `dong_trong_24h` từ `ticket_closed` và kiểm tra không có event `ticket_reopened` trong 7 ngày theo cùng `trace_id`.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm các event `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia cho tổng số event `staff_review_decision`.
- **Chỉ số an toàn (Lỗi lọt đến khách):** Đếm số event `ticket_reopened` có `mo_lai_trong_7_ngay == 1` chia cho tổng số event `refund_request_created`.
- **Chỉ số tự đề xuất:** Dùng event `staff_review_decision` (`quyet_dinh == 'giu'`) và `audit_sample_checked` (đối soát hàng tuần).

## E2 · Rủi ro kinh tế

Dữ liệu định lượng trích xuất từ bảng độ nhạy [bang_chi_phi.md](bang_chi_phi.md):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%** (từ 4.472 đ lên **6.787 đ** [simulated]) | Tỉ lệ đơn làm lại theo tuần > 7% trong phạm vi pilot (chạy thử là 4,9%) | Thu hẹp phạm vi về `noi_dia`, tạm dừng `hang_nang` và rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Bắt buộc xem lại 100% kéo dài | Chi phí tăng vọt lên **11.743 đ – 12.516 đ** ($0,98\times – 1,04\times$ mức 12.000 đ [simulated]), triệt tiêu giá trị kinh tế | Tỉ lệ yêu cầu cần xem lại vẫn > 50% ở cuối bước rollout 0.25 | Thiết lập ngưỡng tự động duyệt cho các ca rủi ro thấp khi tỉ lệ sửa/bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 tr/tháng làm tăng thêm **2.370 đ/việc** nếu khối lượng giảm 50% (lên 5.784 đ = 0,48× [simulated]) | Tổng lượng yêu cầu thực tế đạt < 50% so với dự báo 45.000 đơn/tháng | Tạm hoãn mở rộng rollout, đàm phán lại chi phí thuê hạ tầng cố định theo khối lượng thực tế | Giám đốc vận hành |
