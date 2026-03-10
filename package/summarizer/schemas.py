json_schema = {
    "title": "PDF 요약",
    "description": "PDF를 텍스트로 변환한 글에 대한 요약",
    "type": "object",
    "properties": {
        "tone": {
            "type": "string",
            "description": "사용자를 위한 PDF 한 줄 요약"
        },
        "description": {
            "type": "string",
            "description": "사용자를 위한 PDF 상세 요약"
        },
        "character": {
            "type": "string",
            "description": "AI 프롬프팅을 위한 PDF 상세요약"
        }
    }
}