# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ThanSet · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: 4.472 đ [simulated] (gấp 16,3 lần hóa đơn token + tool 274,7 đ). Phạm vi pilot (`noi_dia` + `hang_nang`): 3.414 đ, cộng chi phí cố định (40 tr/tháng ở 45k YC/tháng) là 4.599 đ [simulated]. | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%, lên 6.787 đ); 2. Tỉ lệ xem lại (+40,7%, lên 6.292 đ); 3. Lương nhân viên (+23,1%, lên 5.506 đ) [simulated]. Giá token ít nhạy nhất (±5,6%). | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Rẻ hơn rõ rệt: `noi_dia` 2.696 đ (0,22× baseline 12.000 đ); `hang_nang` 8.221 đ (0,69×). Cả hệ thống có cố định đạt 4.599 đ (0,38×) [simulated]. Loại bỏ `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×). | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chạy thử 2 tuần (1.200 YC): Chỉ số chính đạt 82,83% (994/1.200); Tỉ lệ bỏ qua gợi ý 27,12% (48/177 ca xem lại); Tỉ lệ lỗi lọt đến khách (mở lại 7 ngày) 4,25% (51/1.200). | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi được gắn nhãn theo Google PAIR (đồng thuận 85%, 17/20 ca). Bảng khắc phục 5 ca đủ 5 loại, có cách phát hiện đo được qua event và vai trò phụ trách. | Xong, có bằng chứng | Trưởng nhóm QA |
| 6 · Pilot plan | Phân bổ theo nhân viên (20 đối chứng + 20 can thiệp, DE = 6,96); chấp nhận đánh đổi MDE 6 điểm (n = 859/nhóm, m ≥ 299 YC/NV; power ở mức 5 điểm là 0,64); 3 luật dừng định lượng có người quyết định. | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Bắt buộc xem lại 100% làm chi phí vọt lên 11.743 đ – 12.516 đ (0,98× – 1,04× baseline 12.000 đ) [simulated]; số ca làm lại tăng gấp đôi đẩy chi phí tăng +51,8% [simulated]. | Giả lập | Giám đốc tài chính |

**Đề xuất:** **Go có điều kiện** cho kế hoạch pilot trợ lý hoàn phí (chỉ áp dụng phạm vi `noi_dia` và `hang_nang` tại 12 depot):

1. **Khắc phục lỗi hệ thống trọng yếu trước ngày mở pilot (hạn 2026-11-30):** Kỹ sư trưởng agent hoàn thành cơ chế đối soát sổ cái hai chiều và khóa chống hoàn trùng (idempotency key) nhằm triệt tiêu hoàn toàn nguy cơ lỗi lặp sổ cái (ca 7, ca 20).
2. **Ký duyệt đánh đổi thống kê (hạn 2026-12-01):** Giám đốc vận hành ký biên bản chấp thuận thiết kế pilot phân bổ theo 40 nhân viên (20 + 20 cụm), chấp nhận phát hiện mức chênh MDE 6 điểm (nếu tác động thật là 5 điểm thì power giảm còn 0,64).
3. **Giám sát thời gian thực và thay thế số giả lập sau tuần đầu (hạn 2026-12-08):** PM trợ lý hoàn phí kiểm tra kích hoạt đủ 8 telemetry events có `trace_id`; sau tuần 1 (rollout 10%), thay thế các con số giả lập `_simulated` bằng số phút đo lường thực tế từ event `staff_review_decision` và `staff_rework_completed` để cập nhật lại mô hình chi phí trước khi chuyển sang bước rollout 25%.
