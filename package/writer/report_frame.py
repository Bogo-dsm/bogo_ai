json_schema = {
    "title": "SchoolProjectReport",
    "type": "object",
    "properties": {
        "document_info": {
            "type": "object",
            "properties": {
                "project_name": {"type": "string"},
                "club_name": {"type": "string"},
                "members": {"type": "array", "items": {"type": "string"}},
                "teacher_name": {"type": "string"}
            },
            "required": ["project_name", "members"]
        },
        "report_body": {
            "type": "object",
            "properties": {
                "motivation": {"type": "string", "description": "1.1 프로젝트 실행 동기 (최대한 상세히)"},
                "purpose": {"type": "string", "description": "1.2 프로젝트 목적 (구체적 목표 포함)"},
                "background": {"type": "string", "description": "2.1 이론적 배경 (YOLO, LSTM 등 기술 원리 포함)"},
                "spec": {"type": "string", "description": "3.1 기능 명세"},
                "server_env": {"type": "string", "description": "3.2 서버 환경"},
                "sw_env": {"type": "string", "description": "3.3 소프트웨어 환경"},
                "architecture": {"type": "string", "description": "3.4 전체 구조 및 아키텍처"},
                "db_design": {"type": "string", "description": "3.5 데이터베이스 설계"},
                "conclusion": {"type": "string", "description": "4.1 결론 및 성과"},
                "suggestion": {"type": "string", "description": "4.2 제언 및 향후 계획"},
                "references": {"type": "string", "description": "5. 참고문헌 리스트"}
            },
            "required": ["motivation", "purpose", "background", "spec", "server_env", "sw_env", "architecture", "db_design", "conclusion", "suggestion", "references"]
        }
    },
    "required": ["document_info", "report_body"]
}