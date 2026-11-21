# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thành Danh · Người gắn nhãn 2: Nguyễn Thị Hồng San (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngầm | Không | Ngữ cảnh |
| 17 | Ngầm | Hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 13 (Giới hạn hệ thống vs Hệ thống):** Yêu cầu hỏi về bảo hiểm của công ty đối tác nằm ngoài phạm vi trợ lý, nên nguyên nhân gốc là **Giới hạn hệ thống** (kể cả khi trợ lý trả lời chung chung thay vì từ chối rõ).
- **Ca 16 (Ngữ cảnh vs Ngầm):** Trợ lý gửi thông báo lúc 2:14 sáng đúng theo thiết kế "gửi ngay khi xong" nhưng khách phản ánh bị làm phiền, nên đây là lỗi **Ngữ cảnh** (giả định thiết kế không khớp hoàn cảnh người dùng), không phải lỗi **Ngầm**.
- **Ca 17 (Ngầm vs Hệ thống):** Bảng giá cũ trong bộ nhớ đệm gây lệch 212 đơn suốt 9 ngày mà cả hệ thống lẫn khách không ai phát hiện cho tới khi kiểm tra, nên là lỗi **Ngầm** thay vì **Hệ thống**.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` theo dõi hằng ngày; cảnh báo khi vượt 2% tổng số yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn nhập đúng mã kèm ảnh minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát theo giờ giữa event `refund_success_notified` và bản ghi sổ cái `ledger_status = ok` theo `trace_id`; ngưỡng 0 ca lệch | Chỉ gửi thông báo "đã hoàn tiền thành công" khi API sổ cái trả `ok`; sau 3 lần lỗi 503 thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ yêu cầu mở lại trong 7 ngày vì lý do số tiền nhưng kiểm tra đối soát thấy tính đúng, đo theo tuần; ngưỡng > 1% | Cập nhật mẫu tin nhắn hoàn tiền luôn hiển thị chi tiết phép tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` theo loại yêu cầu, đo hằng ngày; cảnh báo khi > 5% ở một loại | Giữ cơ chế báo rõ thiếu dữ liệu và chuyển nhân viên kèm tóm tắt; loại yêu cầu `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá hiện hành; ngưỡng > 1% đơn lệch số tiền | Xóa bộ nhớ đệm tự động khi cập nhật bảng giá mới và ghi `pricing_version` vào `trace_id` để truy vết | Kế toán trưởng |
