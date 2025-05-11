import azure.functions as func
import json

# 🔧 You must define this first
app = func.FunctionApp()

# ✅ Now use it
@app.function_name(name="stats")
@app.route(route="stats", auth_level=func.AuthLevel.ANONYMOUS)
def main(req: func.HttpRequest) -> func.HttpResponse:
    mock_data = {
        "hashrate": {"30min": 39.45, "3h": 41.27, "24h": 39.34},
        "earnings": {"1h": 7.02, "12h": 83.31, "24h": 170.29},
        "hashrateTimeline": {
            "labels": ["00:00", "03:00", "06:00", "09:00", "12:00"],
            "values": [38, 41, 39, 40, 39.5]
        }
    }
    return func.HttpResponse(json.dumps(mock_data), mimetype="application/json")
