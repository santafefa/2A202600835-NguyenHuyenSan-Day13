# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: Individual (Nguyen Huyen San)
- [REPO_URL]: https://github.com/your-username/day13-observability-lab
- [MEMBERS]:
  - Member A: Nguyen Huyen San | Role: Fullstack Observability (Logging, Tracing, Alerts, Dashboard, Report)

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 15
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: ./correlation_id_and_pii.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: ./correlation_id_and_pii.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: ./langfuse_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: Trong Langfuse, Trace Waterfall cho thấy request được chia thành 2 span chính: `retrieve` (tương tác với RAG) và `generate` (tương tác với LLM). Nhìn vào đây có thể thấy rõ thời gian chủ yếu bị delay ở LLM span trong khi RAG span tốn rất ít thời gian.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: ./dashboard_6_panels.png
- [SLO_TABLE]:

| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | `< 3000ms` | 28d | 2450ms |
| Error Rate | `< 2%` | 28d | 0.0% |
| Cost Budget | `< $2.5/day` | 1d | $1.25 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: ./alert1.png, ./alert2.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#4-low-quality-score

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Độ trễ (Latency P95) tăng vọt vượt ngưỡng 5000ms, hệ thống báo động `high_latency_p95`.
- [ROOT_CAUSE_PROVED_BY]: Trace ID trên Langfuse cho thấy span `retrieve` (RAG) bị nghẽn và chiếm hơn 4500ms tổng thời gian của request.
- [FIX_ACTION]: Tắt toggle `rag_slow` bằng API `/incidents/rag_slow/disable`.
- [PREVENTIVE_MEASURE]: Cấu hình timeout cứng cho RAG component (ví dụ: max 2000ms). Bổ sung cơ chế fallback (trả về kết quả rỗng thay vì block toàn bộ quá trình sinh text) nếu vector DB quá tải.

---

## 5. Individual Contributions & Evidence

### Nguyen Huyen San
- [TASKS_COMPLETED]: Hoàn thành toàn bộ Lab. (1) Xây dựng `CorrelationIdMiddleware` với `clear_contextvars()` để tránh rò rỉ context. (2) Viết processor `scrub_event` tự động che PII. (3) Cấu hình Custom Metric cảnh báo `low_quality_score` và viết Runbook. (4) Tích hợp Langfuse và setup Dashboard 6 Panels.
- [EVIDENCE_LINK]: https://github.com/your-username/day13-observability-lab/commits/main

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: **Cơ chế Caching (+3đ)**: Thêm từ điển `_CACHE` vào `app/agent.py`. Trả kết quả từ Cache cho các câu hỏi trùng lặp với `cost_usd = 0.0` và `latency_ms = 1`, giảm tải đáng kể cho LLM.
- [BONUS_AUDIT_LOGS]: **Audit Logs Tách Rời (+2đ)**: Thêm hàm `write_audit_log` ghi file riêng. Mọi thao tác rủi ro (bật/tắt incident) được lưu trực tiếp vào `data/audit.jsonl` để bảo mật.
- [BONUS_CUSTOM_METRIC]: **Chỉ số Chất lượng & Dashboard Đẹp (+5đ)**: Bổ sung custom metric `quality_avg` & alert `low_quality_score`. Tự lập trình giao diện Dashboard HTML/Chart.js chuyên nghiệp trực tiếp trên FastAPI.
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: ./correlation_id_and_pii.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: ./langfuse_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: Trong Langfuse, Trace Waterfall cho thấy request được chia thành 2 span chính: `retrieve` (tương tác với RAG) và `generate` (tương tác với LLM). Nhìn vào đây có thể thấy rõ thời gian chủ yếu bị delay ở LLM span trong khi RAG span tốn rất ít thời gian.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: ./dashboard_6_panels.png
- [SLO_TABLE]:

| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | `< 3000ms` | 28d | 2450ms |
| Error Rate | `< 2%` | 28d | 0.0% |
| Cost Budget | `< $2.5/day` | 1d | $1.25 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: ./alert1.png, ./alert2.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#4-low-quality-score

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Độ trễ (Latency P95) tăng vọt vượt ngưỡng 5000ms, hệ thống báo động `high_latency_p95`.
- [ROOT_CAUSE_PROVED_BY]: Trace ID trên Langfuse cho thấy span `retrieve` (RAG) bị nghẽn và chiếm hơn 4500ms tổng thời gian của request.
- [FIX_ACTION]: Tắt toggle `rag_slow` bằng API `/incidents/rag_slow/disable`.
- [PREVENTIVE_MEASURE]: Cấu hình timeout cứng cho RAG component (ví dụ: max 2000ms). Bổ sung cơ chế fallback (trả về kết quả rỗng thay vì block toàn bộ quá trình sinh text) nếu vector DB quá tải.

---

## 5. Individual Contributions & Evidence

### Nguyen Huyen San
- [TASKS_COMPLETED]: Hoàn thành toàn bộ Lab. (1) Xây dựng `CorrelationIdMiddleware` với `clear_contextvars()` để tránh rò rỉ context. (2) Viết processor `scrub_event` tự động che PII. (3) Cấu hình Custom Metric cảnh báo `low_quality_score` và viết Runbook. (4) Tích hợp Langfuse và setup Dashboard 6 Panels.
- [EVIDENCE_LINK]: https://github.com/your-username/day13-observability-lab/commits/main

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: **Cơ chế Caching (+3đ)**: Thêm từ điển `_CACHE` vào `app/agent.py`. Trả kết quả từ Cache cho các câu hỏi trùng lặp với `cost_usd = 0.0` và `latency_ms = 1`, giảm tải đáng kể cho LLM.
- [BONUS_AUDIT_LOGS]: **Audit Logs Tách Rời (+2đ)**: Thêm hàm `write_audit_log` ghi file riêng. Mọi thao tác rủi ro (bật/tắt incident) được lưu trực tiếp vào `data/audit.jsonl` để bảo mật.
- [BONUS_CUSTOM_METRIC]: **Chỉ số Chất lượng & Dashboard Đẹp (+5đ)**: Bổ sung custom metric `quality_avg` & alert `low_quality_score`. Tự lập trình giao diện Dashboard HTML/Chart.js chuyên nghiệp trực tiếp trên FastAPI.
- [TRACE_WATERFALL_EXPLANATION]: Trong Langfuse, Trace Waterfall cho thấy request được chia thành 2 span chính: `retrieve` (tương tác với RAG) và `generate` (tương tác với LLM). Nhìn vào đây có thể thấy rõ thời gian chủ yếu bị delay ở LLM span trong khi RAG span tốn rất ít thời gian.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: ./dashboard_6_panels.png
- [SLO_TABLE]:

| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | `< 3000ms` | 28d | 2450ms |
| Error Rate | `< 2%` | 28d | 0.0% |
| Cost Budget | `< $2.5/day` | 1d | $1.25 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: ./alert1.png, ./alert2.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#4-low-quality-score

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Độ trễ (Latency P95) tăng vọt vượt ngưỡng 5000ms, hệ thống báo động `high_latency_p95`.
- [ROOT_CAUSE_PROVED_BY]: Trace ID trên Langfuse cho thấy span `retrieve` (RAG) bị nghẽn và chiếm hơn 4500ms tổng thời gian của request.
- [FIX_ACTION]: Tắt toggle `rag_slow` bằng API `/incidents/rag_slow/disable`.
- [PREVENTIVE_MEASURE]: Cấu hình timeout cứng cho RAG component (ví dụ: max 2000ms). Bổ sung cơ chế fallback (trả về kết quả rỗng thay vì block toàn bộ quá trình sinh text) nếu vector DB quá tải.

---

## 5. Individual Contributions & Evidence

### Nguyen Huyen San
- [TASKS_COMPLETED]: Hoàn thành toàn bộ Lab với vai trò cá nhân.
  1. **Middleware & Logs Context**: Xây dựng `CorrelationIdMiddleware`, xử lý `bind_contextvars` gộp các thông tin `user_id_hash`, `session_id`, `feature`, `model` vào log payload.
  2. **PII Scrubbing**: Viết structlog processor (`scrub_event`) để ẩn các dữ liệu nhạy cảm (email, credit card) trong payload.
  3. **Alerting & Runbooks**: Bổ sung cảnh báo Custom Metric (`low_quality_score`) và tài liệu Runbook xử lý.
  4. **Langfuse & Dashboard**: Load test để sinh dữ liệu, xem xét Traces trên Langfuse và thiết lập Dashboard 6 Panels (Latency, Traffic, Cost, Token, Errors, Quality).

- [EVIDENCE_LINK]: https://github.com/your-username/day13-observability-lab/commits/main
- [DEEP_DIVE_EXPLANATION]: Trong middleware, phải gọi `clear_contextvars()` trước mỗi request để tránh rò rỉ context giữa các requests (do tính chất bất đồng bộ của FastAPI). Về PII scrubber, tích hợp vào structlog processor giúp tự động hóa việc che giấu dữ liệu cho toàn bộ ứng dụng, thay vì phải format thủ công ở từng điểm ghi log.

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: **Cơ chế Caching (+3đ)**: Đã thêm từ điển `_CACHE` vào `app/agent.py`. Nếu người dùng hỏi trùng lặp một câu hỏi trước đó, hệ thống lập tức trả về kết quả từ Cache với `cost_usd = 0.0` và `latency_ms = 1`. Giảm tải LLM và chi phí một cách rõ rệt.
- [BONUS_AUDIT_LOGS]: **Audit Logs Tách Rời (+2đ)**: Đã phát triển hàm `write_audit_log` ghi file riêng. Mọi hành động thao tác hệ thống mang tính rủi ro (như bật/tắt incident) đều được ghi nhận trực tiếp vào file `data/audit.jsonl` đáp ứng yêu cầu lưu trữ log bảo mật.
- [BONUS_CUSTOM_METRIC]: **Chỉ số Chất lượng & Dashboard Đẹp (+5đ)**: Bổ sung custom metric `quality_avg` và luật alert `low_quality_score`. Hơn nữa, tự lập trình giao diện Dashboard HTML/Chart.js chuyên nghiệp trực tiếp trên FastAPI thay vì dùng công cụ ngoài.
