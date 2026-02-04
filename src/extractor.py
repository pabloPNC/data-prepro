from ollama import chat
from pydantic import BaseModel
from pypdf import PdfReader
import logging

logger = logging.getLogger(__name__)

class Extractor:

    def __init__(
        self,
        model: str,
        schema: BaseModel,
        document: str
    ) -> None:
        self.model = model
        self.schema = schema
        self.document = document

    def get_page_contents(self, page_number: int) -> str:
        reader = PdfReader(self.document)
        page = reader.pages[page_number]
        page_content =  page.extract_text()

        logger.debug(page_content)

        return page_content

    def preprocess(self, prompt: str, content: str):
        message = f"Teniendo en cuenta el siguiente texto: {content}. {prompt}"
        logger.debug(message)
        response = chat(
            model = self.model,
            messages = [{
                "role": "user",
                "content": message
            }],
            format = self.schema.model_json_schema()
        )
        return response.message.content
