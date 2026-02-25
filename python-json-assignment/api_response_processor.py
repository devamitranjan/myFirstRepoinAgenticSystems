import json
from typing import Any, Dict


def main() -> None:
    api_response_json = """
    {
      "id": "req_123",
      "status": "success",
      "result": {
        "text": "Hello world",
        "confidence": 0.98
      }
    }
    """

    # Parse JSON string into Python objects
    response: Dict[str, Any] = json.loads(api_response_json)

    # Extract values without hardcoding them
    request_id = response.get("id")
    status = response.get("status")

    result = response.get("result", {})
    text_result = result.get("text")
    confidence = result.get("confidence")

    # Print extracted values
    print(f"Request ID: {request_id}")
    print(f"Status: {status}")
    print(f"Text: {text_result}")
    print(f"Confidence: {confidence}")

    # Warning if confidence is below threshold
    if isinstance(confidence, (int, float)) and confidence < 0.9:
        print("Warning: Confidence score is below 0.9")

    # New Python dictionary representing a follow-up result
    follow_up_result: Dict[str, Any] = {
        "original_request_id": request_id,
        "status": "processed",
        "follow_up": {
            "summary": text_result,
            "confidence": confidence,
        },
    }

    # Convert Python dictionary to JSON string
    follow_up_json = json.dumps(follow_up_result, indent=2)

    # Write JSON output to a file named response.json
    with open("response.json", "w", encoding="utf-8") as f:
        f.write(follow_up_json)


if __name__ == "__main__":
    main()

