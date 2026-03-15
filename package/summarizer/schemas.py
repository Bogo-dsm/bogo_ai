json_schema = {
    "title": "PDF_Summary",
    "description": "보고서 양식 전이를 위한 보고서 요약",
    "type": "object",
    "properties": {
        "tone": {
            "type": "string",
            "description": "사용자를 위한 보고서 특징 한 줄 요약"
        },
        "desc": {
            "type": "string",
            "description": "사용자를 위한 보고서 특징 상세 요약"
        },
        "character": {
            "type": "string",
            "description": "양식 전이를 위한 AI 프롬프팅용 보고서 특징 상세요약"
        }
    },
    "required": ["tone", "desc", "character"]
}