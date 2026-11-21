# Team

## Thông tin nhóm

- Tên nhóm: ThanSet
- Lớp: L3A
- Repo nhóm: `K5-L3A-Day13-ThanSet-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/HDang3825/K5-L3A-Day13-ThanSet-LaunchEconomics (đang làm việc trên các nhánh thành viên, sẽ chốt nhánh `main` trước khi nộp)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |        |      |       |        | Người viết code (nửa đầu) |
|   2 | Lưu Đăng Tuấn | 2A202603454 | 26ai.tuanld@vinuni.edu.vn | kegacua | Người kiểm số (nửa đầu) / Người viết code (nửa sau) |
|   3 |        |      |       |        | Người gắn nhãn 1 |
|   4 |        |      |       |        | Người gắn nhãn 2, kiêm giữ hồ sơ |

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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

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
