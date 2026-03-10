json_schema = {
    "title": "SchoolProjectReport",
    "description": "대덕소프트웨어마이스터고등학교 학교장 인증제 프로젝트 보고서 양식",
    "type": "object",
    "properties": {
        "document_info": {
            "type": "object",
            "description": "문서의 기본 정보 및 스타일 설정",
            "properties": {
                "school": {"type": "string", "description": "학교명 (기본값: 대덕소프트웨어마이스터고등학교)"},
                "project_name": {"type": "string", "description": "프로젝트의 전체 제목"},
                "club_name": {"type": "string", "description": "소속 동아리명 (없을 경우 null)"},
                "members": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string", "description": "학번 (예: 1101)"},
                            "name": {"type": "string", "description": "학생 성명"}
                        }
                    }
                },
                "teacher_name": {"type": "string", "description": "지도 교사 성함"},
                "styles": {
                    "type": "object",
                    "properties": {
                        "font": {"type": "string", "description": "사용 폰트 (예: 휴먼명조)"},
                        "font_size": {"type": "integer", "description": "본문 글자 크기 (기본: 12)"},
                        "line_height": {"type": "number", "description": "줄 간격 (기본: 1.6)"}
                    }
                }
            },
            "required": ["school", "project_name", "members"]
        },
        "sections": {
            "type": "array",
            "description": "보고서의 각 주요 섹션 리스트 (Ⅰ, Ⅱ, Ⅲ, Ⅳ)",
            "items": {
                "type": "object",
                "properties": {
                    "section_id": {"type": "string", "description": "섹션 식별자 (예: 1_introduction)"},
                    "title": {"type": "string", "description": "섹션의 대제목 (예: Ⅰ. 프로젝트 실행 동기 및 목적)"},
                    "contents": {
                        "type": "array",
                        "description": "섹션 내부에 들어갈 소제목 및 본문 문단들",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["subtitle", "paragraph", "motivation", "purpose"],
                                    "description": "콘텐츠의 성격 (소제목, 일반 문단, 동기, 목적 등)"
                                },
                                "text": {
                                    "type": "string",
                                    "description": "실제 텍스트 내용. 반드시 '평어체(~이다, ~함)'로 작성하며, 구체적이고 전문적인 용어를 사용해야 함."
                                },
                                "image": {
                                    "type": ["string", "null"],
                                    "description": "이미지가 필요한 위치에 '그림 X' 형식으로 표기. 필요 없으면 null."
                                }
                            },
                            "required": ["type", "text"]
                        }
                    }
                },
                "required": ["section_id", "title", "contents"]
            }
        },
        "references": {
            "type": "array",
            "description": "참고 문헌 리스트",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "description": "출처 유형 (web, book, paper 등)"},
                    "formatted_text": {"type": "string", "description": "표준 참고문헌 작성법에 따른 텍스트"}
                }
            }
        }
    },
    "required": ["document_info", "sections"]
}
