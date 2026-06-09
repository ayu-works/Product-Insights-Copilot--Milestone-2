<details class="js-checks-log-group"><summary><span class="">Run if [ -n "" ]; then
</span></summary>

</details>

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:22){"run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "iso_week": "2026-W23", "resume_from": "ingest", "previous_status": null, "event": "pulse_run_start", "level": "info", "logger": "agent.orchestrator", "timestamp": "2026-06-09T09:15:10.190820Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:23){"path": "data/pulse.db", "event": "db_initialised", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.storage", "timestamp": "2026-06-09T09:15:10.191415Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:24){"product": "groww", "weeks": 10, "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "event": "ingest_start", "level": "info", "logger": "agent.__main__", "timestamp": "2026-06-09T09:15:10.247578Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:25){"path": "data/pulse.db", "event": "db_initialised", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.storage", "timestamp": "2026-06-09T09:15:10.248158Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:26)HTTP Request: GET [https://itunes.apple.com/in/rss/customerreviews/page=1/id=1404871982/sortby=mostrecent/json](https://itunes.apple.com/in/rss/customerreviews/page=1/id=1404871982/sortby=mostrecent/json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:27){"product": "groww", "country": "in", "event": "appstore_zero_reviews", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "level": "warning", "logger": "agent.ingestion.appstore", "timestamp": "2026-06-09T09:15:11.112893Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:28){"product": "groww", "count": 0, "event": "appstore_fetched", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "level": "info", "logger": "agent.ingestion.appstore", "timestamp": "2026-06-09T09:15:11.113101Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:29){"product": "groww", "pages": 25, "count": 5000, "cutoff": "2026-03-31", "event": "playstore_fetched", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "level": "info", "logger": "agent.ingestion.playstore", "timestamp": "2026-06-09T09:15:22.950782Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:30){"total": 5000, "event": "ingest_raw_count", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.__main__", "timestamp": "2026-06-09T09:15:22.951026Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:31){"filtered": 3638, "kept": 1362, "event": "ingest_filtered", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.__main__", "timestamp": "2026-06-09T09:15:27.399339Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:32){"run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "inserts": 1362, "updates": 0, "audit": "data/raw/groww/ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c.jsonl", "event": "ingest_complete", "product": "groww", "level": "info", "logger": "agent.__main__", "timestamp": "2026-06-09T09:15:27.419810Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:33)Ingested 1362 new reviews (0 updated) for groww — run ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:34){"path": "data/pulse.db", "event": "db_initialised", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.storage", "timestamp": "2026-06-09T09:15:27.429386Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:35){"count": 1362, "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "event": "cluster_reviews_loaded", "product": "groww", "level": "info", "logger": "agent.__main__", "timestamp": "2026-06-09T09:15:27.436861Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:36)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:37)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/modules.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:38)Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:39)Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:40)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/modules.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:41)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/modules.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:42)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config_sentence_transformers.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:43)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:44)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:45)Loading SentenceTransformer model from BAAI/bge-small-en-v1.5.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:46)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config_sentence_transformers.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:47)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:48)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/README.md](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:49)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/README.md](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:50)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/README.md](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:51)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/modules.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:52)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/modules.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:53)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/sentence_bert_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:54)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:55)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:56)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/adapter_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:57)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:58)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:59)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:60)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/model.safetensors](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/model.safetensors) "HTTP/1.1 302 Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:61)HTTP Request: GET [https://huggingface.co/api/models/BAAI/bge-small-en-v1.5/xet-read-token/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a](https://huggingface.co/api/models/BAAI/bge-small-en-v1.5/xet-read-token/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:63)Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:64)Loading weights: 100%|██████████| 199/199 [00:00<00:00, 4314.19it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:65)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/processor_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:66)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/preprocessor_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:67)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/video_preprocessor_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:68)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/preprocessor_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:69)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:70)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:71)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:72)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:73)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:74)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:75)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:76)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer_config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:77)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:78)HTTP Request: GET [https://huggingface.co/api/models/BAAI/bge-small-en-v1.5/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/BAAI/bge-small-en-v1.5/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:79)HTTP Request: GET [https://huggingface.co/api/models/BAAI/bge-small-en-v1.5/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/BAAI/bge-small-en-v1.5/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:80)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/vocab.txt](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/vocab.txt) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:81)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/vocab.txt](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/vocab.txt) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:82)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/vocab.txt](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/vocab.txt) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:83)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:84)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:85)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/tokenizer.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:86)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/added_tokens.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/added_tokens.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:87)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/special_tokens_map.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/special_tokens_map.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:88)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/special_tokens_map.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/special_tokens_map.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:89)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/special_tokens_map.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/special_tokens_map.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:90)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/chat_template.jinja](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/chat_template.jinja) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:91)HTTP Request: HEAD [https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/1_Pooling/config.json](https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:92)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:93)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/BAAI/bge-small-en-v1.5/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:94)HTTP Request: GET [https://huggingface.co/api/models/BAAI/bge-small-en-v1.5](https://huggingface.co/api/models/BAAI/bge-small-en-v1.5) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:95){"removed": 45, "kept": 1317, "event": "clustering_filter", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.clustering.pipeline", "timestamp": "2026-06-09T09:15:45.406274Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:96){"hits": 0, "misses": 1317, "event": "embedding_cache_lookup", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.clustering.embeddings", "timestamp": "2026-06-09T09:15:45.407849Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:97){"embedding_cache_hits": 0, "embedding_cache_misses": 1317, "event": "embedding_cache_hits", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.clustering.embeddings", "timestamp": "2026-06-09T09:16:03.153376Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:98)/Users/runner/work/Product-Insights-Copilot--Milestone-2/Product-Insights-Copilot--Milestone-2/phases/phase-7-orchestration/.venv/lib/python3.11/site-packages/umap/umap_.py:1952: UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:99)  warn(

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:100)/Users/runner/work/Product-Insights-Copilot--Milestone-2/Product-Insights-Copilot--Milestone-2/phases/phase-7-orchestration/.venv/lib/python3.11/site-packages/sklearn/cluster/_hdbscan/hdbscan.py:722: FutureWarning: The default value of `copy` will change from False to True in 1.10. Explicitly set a value for `copy` to silence this warning.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:101)  warn(

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:102){"clusters": 23, "noise": 430, "total": 1317, "event": "hdbscan_result", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.clustering.pipeline", "timestamp": "2026-06-09T09:16:23.471331Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:103)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:104)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:105)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:106)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:107)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:108)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:109)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:110)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:111)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:112)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:113)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:114)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:115)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:116)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:117)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:118)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:119)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:120)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:121)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:122)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:123)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:124)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:125)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/model.safetensors](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/model.safetensors) "HTTP/1.1 302 Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:126)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/xet-read-token/1110a243fdf4706b3f48f1d95db1a4f5529b4d41](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/xet-read-token/1110a243fdf4706b3f48f1d95db1a4f5529b4d41) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:128)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:129)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 20592.66it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:130)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:131)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:132)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:133)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:134)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:135)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:136)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:137)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:138)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:139)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:140)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:141)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:142)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:143)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:144)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:145)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/vocab.txt](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/vocab.txt) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:146)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/vocab.txt](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/vocab.txt) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:147)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/vocab.txt](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/vocab.txt) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:148)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:149)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:150)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:151)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/added_tokens.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/added_tokens.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:152)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/special_tokens_map.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/special_tokens_map.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:153)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/special_tokens_map.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/special_tokens_map.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:154)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/special_tokens_map.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/special_tokens_map.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:155)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/chat_template.jinja](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/chat_template.jinja) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:156)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:157)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:158)HTTP Request: GET [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:159)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:160)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:161)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:162)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:163)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:164)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:165)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:166)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:167)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:168)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:169)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:170)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:171)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:172)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:173)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:174)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:175)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:176)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:178)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:179)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 22818.01it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:180)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:181)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:182)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:183)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:184)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:185)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:186)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:187)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:188)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:189)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:190)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:191)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:192)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:193)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:194)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:195)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:196)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:197)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:198)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:199)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:200)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:201)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:202)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:203)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:204)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:205)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:206)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:207)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:208)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:209)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:210)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:211)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:212)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:213)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:214)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:215)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 9430.34it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:216)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:217)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:218)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:220)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:221)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:222)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:223)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:224)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:225)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:226)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:227)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:228)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:229)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:230)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:231)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:232)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:233)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:234)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:235)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:236)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:237)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:238)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:239)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:240)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:241)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:242)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:243)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:244)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:245)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:246)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:247)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:248)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:249)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:250)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:251)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:252)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 5416.82it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:253)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:254)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:255)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:256)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:257)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:258)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:259)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:260)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:261)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:262)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:264)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:265)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:266)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:267)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:268)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:269)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:270)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:271)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:272)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:273)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:274)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:275)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:276)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:277)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:278)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:279)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:280)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:281)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:282)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:283)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:284)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:285)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:286)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:287)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:288)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:289)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 21089.25it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:290)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:291)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:292)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:293)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:294)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:295)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:296)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:297)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:298)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:299)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:300)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:301)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:303)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:304)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:305)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:306)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:307)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:308)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:309)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:310)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:311)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:312)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:313)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:314)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:315)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:316)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:317)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:318)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:319)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:320)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:321)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:322)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:323)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:324)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:325)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:326)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 22617.31it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:327)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:328)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:329)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:330)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:331)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:332)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:334)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:335)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:336)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:337)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:338)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:339)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:340)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:341)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:342)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:343)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:344)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:345)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:346)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:347)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:348)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:349)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:350)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:351)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:352)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:353)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:354)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:355)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:356)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:357)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:358)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:359)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:360)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:361)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:362)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:363)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 20287.08it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:364)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:365)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:366)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:367)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:368)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:369)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:371)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:372)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:373)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:374)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:375)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:376)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:377)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:378)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:379)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:380)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:381)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:382)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:383)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:384)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:385)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:386)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:387)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:388)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:389)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:390)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:391)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:392)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:393)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:394)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:395)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:396)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:397)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:398)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:399)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:400)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 18458.16it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:401)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:402)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:403)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:404)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:405)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:406)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:407)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:408)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:409)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:410)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:411)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:413)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:414)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:415)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:416)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:417)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:418)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:419)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:420)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:421)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:422)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:423)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:424)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:425)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:426)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:427)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:428)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:429)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:430)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:431)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:432)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:433)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:434)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:435)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:436)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:437)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 19798.96it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:438)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:439)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:441)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:442)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:443)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:444)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:445)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:446)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:447)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:448)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:449)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:450)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:451)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:452)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:453)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:454)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:455)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:456)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:457)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:458)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:459)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:460)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:461)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:462)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:463)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:464)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:465)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:466)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:467)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:468)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:469)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:470)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:471)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:472)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:473)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:474)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 8984.74it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:475)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:476)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:477)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:479)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:480)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:481)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:482)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:483)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:484)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:485)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:486)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:487)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:488)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:489)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:490)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:491)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:492)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:493)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:494)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:495)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:496)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:497)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:498)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:499)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:500)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:501)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:502)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:503)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:504)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:505)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:506)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:507)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:508)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:509)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:510)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:511)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 11882.53it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:512)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:513)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:514)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:515)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:516)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:517)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:519)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:520)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:521)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:522)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:523)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:524)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:525)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:526)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:527)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:528)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:529)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:530)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:531)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:532)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:533)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:534)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:535)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:536)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:537)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:538)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:539)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:540)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:541)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:542)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:543)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:544)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:545)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:546)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:547)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:548)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 16431.98it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:549)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:550)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:551)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:552)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:553)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:554)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:555)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:556)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:557)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:559)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:560)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:561)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:562)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:563)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:564)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:565)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:566)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:567)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:568)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:569)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:570)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:571)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:572)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:573)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:574)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:575)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:576)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:577)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:578)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:579)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:580)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:581)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:582)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:583)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:584)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:585)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 15279.53it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:587)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:588)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:589)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:590)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:591)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:592)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:593)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:594)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:595)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:596)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:597)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:598)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:599)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:600)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:601)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:602)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:603)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:604)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:605)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:606)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:607)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:608)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:609)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:610)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:611)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:612)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:613)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:614)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:615)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:616)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:617)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:618)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:619)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:620)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:621)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:622)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 10740.45it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:624)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:625)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:626)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:627)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:628)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:629)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:630)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:631)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:632)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:633)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:634)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:635)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:636)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:637)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:638)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:639)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:640)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:641)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:642)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:643)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:644)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:645)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:646)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:647)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:648)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:649)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:650)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:651)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:652)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:653)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:654)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:655)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:656)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:657)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:658)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:659)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 18947.12it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:660)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:661)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:662)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:663)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:664)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:665)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:666)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:667)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:669)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:670)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:671)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:672)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:673)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:674)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:675)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:676)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:677)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:678)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:679)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:680)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:681)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:682)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:683)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:684)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:685)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:686)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:687)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:688)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:689)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:690)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:691)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:692)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:693)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:694)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:695)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:696)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 11630.77it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:698)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:699)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:700)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:701)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:702)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:703)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:704)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:705)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:706)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:707)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:708)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:709)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:710)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:711)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:712)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:713)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:714)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:715)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:716)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:717)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:718)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:719)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:720)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:721)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:722)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:723)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:724)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:725)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:726)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:727)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:728)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:729)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:730)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:731)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:732)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:733)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 5833.45it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:734)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:736)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:737)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:738)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:739)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:740)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:741)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:742)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:743)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:744)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:745)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:746)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:747)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:748)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:749)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:750)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:751)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:752)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:753)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:754)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:755)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:756)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:757)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:758)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:759)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:760)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:761)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:762)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:763)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:764)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:765)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:766)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:767)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:768)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:769)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:770)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 16591.01it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:771)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:772)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:774)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:775)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:776)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:777)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:778)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:779)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:780)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:781)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:782)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:783)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:784)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:785)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:786)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:787)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:788)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:789)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:790)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:791)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:792)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:793)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:794)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:795)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:796)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:797)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:798)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:799)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:800)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:801)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:802)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:803)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:804)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:805)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:806)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:807)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 17290.22it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:808)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:809)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:810)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:811)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:812)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:813)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:814)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:815)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:817)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:818)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:819)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:820)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:821)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:822)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:823)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:824)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:825)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:826)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:827)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:828)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:829)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:830)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:831)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:832)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:833)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:834)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:835)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:836)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:837)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:838)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:839)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:840)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:841)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:842)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:843)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:844)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 15727.88it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:845)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:847)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:848)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:849)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:850)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:851)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:852)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:853)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:854)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:855)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:856)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:857)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:858)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:859)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:860)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:861)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:862)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:863)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:864)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:865)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:866)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:867)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:868)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:869)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:870)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:871)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:872)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:873)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:874)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:875)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:876)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:877)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:878)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:879)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:880)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:881)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 14015.49it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:882)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:884)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:885)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:886)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:887)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:888)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:889)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:890)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:891)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:892)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:893)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:894)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:895)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:896)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:897)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:898)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:899)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:900)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:901)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:902)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:903)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:904)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:905)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:906)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:907)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:908)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:909)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:910)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:911)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:912)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:913)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:914)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:915)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:916)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:917)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:918)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 15275.20it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:920)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:921)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:922)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:923)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:924)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:925)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:926)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:927)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:928)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:929)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:930)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:931)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:932)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:933)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:934)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:935)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:936)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:937)No device provided, using mps

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:938)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:939)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:940)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:941)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:942)Loading SentenceTransformer model from sentence-transformers/all-MiniLM-L6-v2.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:943)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config_sentence_transformers.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:944)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config_sentence_transformers.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:945)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/README.md) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:946)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/README.md) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:947)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/modules.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:948)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/modules.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:949)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/sentence_bert_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:950)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/sentence_bert_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:951)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/adapter_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:952)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:953)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:954)Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:955)Loading weights: 100%|██████████| 103/103 [00:00<00:00, 17511.69it/s]

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:956)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/processor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:958)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:959)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/video_preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:960)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/preprocessor_config.json) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:961)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:962)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:963)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:964)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:965)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:966)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:967)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer_config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:968)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/tokenizer_config.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:969)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main/additional_chat_templates?recursive=false&expand=false) "HTTP/1.1 404 Not Found"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:970)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&amp;expand=false](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2/tree/main?recursive=true&expand=false) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:971)HTTP Request: HEAD [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/1_Pooling/config.json) "HTTP/1.1 307 Temporary Redirect"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:972)HTTP Request: HEAD [https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json](https://huggingface.co/api/resolve-cache/models/sentence-transformers/all-MiniLM-L6-v2/1110a243fdf4706b3f48f1d95db1a4f5529b4d41/1_Pooling%2Fconfig.json) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:973)HTTP Request: GET [https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2) "HTTP/1.1 200 OK"

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:974){"count": 430, "event": "clustering_noise_reviews", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.clustering.pipeline", "timestamp": "2026-06-09T09:17:35.014705Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:975){"run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "clusters": 23, "noise": 430, "total_reviews": 1317, "event": "clustering_complete", "product": "groww", "level": "info", "logger": "agent.clustering.pipeline", "timestamp": "2026-06-09T09:17:35.038001Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:976)Clustered 1362 reviews into 23 clusters for run ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c (provider=local)

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:977){"path": "data/pulse.db", "event": "db_initialised", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "info", "logger": "agent.storage", "timestamp": "2026-06-09T09:17:35.079635Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:978)Retrying request to /chat/completions in 0.452941 seconds

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:979)Retrying request to /chat/completions in 0.762477 seconds

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:980){"provider": "groq", "model": "llama-3.3-70b-versatile", "attempt": 1, "wait": 5.0, "error": "Connection error.", "event": "llm_retry", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "warning", "logger": "agent.summarization.client", "timestamp": "2026-06-09T09:17:37.529161Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:981)Retrying request to /chat/completions in 0.466840 seconds

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:982)Retrying request to /chat/completions in 0.945135 seconds

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:983){"provider": "groq", "model": "llama-3.3-70b-versatile", "attempt": 2, "wait": 10.0, "error": "Connection error.", "event": "llm_retry", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "warning", "logger": "agent.summarization.client", "timestamp": "2026-06-09T09:17:44.314377Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:984)Retrying request to /chat/completions in 0.414441 seconds

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:985)Retrying request to /chat/completions in 0.855393 seconds

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:986){"provider": "groq", "model": "llama-3.3-70b-versatile", "attempt": 3, "wait": 20.0, "error": "Connection error.", "event": "llm_retry", "run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "product": "groww", "level": "warning", "logger": "agent.summarization.client", "timestamp": "2026-06-09T09:17:55.982857Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:987){"run_id": "ee27c1a2ab7d7c3412b4b0f59457ea5befcfe48c", "step": "summarize", "error": "Groq call 'label_theme' failed after 3 retries: Connection error.", "event": "pulse_run_step_failed", "product": "groww", "level": "error", "logger": "agent.orchestrator", "timestamp": "2026-06-09T09:17:56.013222Z"}

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:988)Run failed: Groq call 'label_theme' failed after 3 retries: Connection error.

[](https://github.com/ayu-works/Product-Insights-Copilot--Milestone-2/actions/runs/27196184991/job/80288303054#step:8:989)Error: Process completed with exit code 1.
