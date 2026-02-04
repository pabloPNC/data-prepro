from src.schemas import Monster
from src.extractor import Extractor
import logging


def main():
    my_extractor = Extractor(
        model = "llama3.2:3b",
        schema = Monster,
        document = "./docs/DnD_BasicRules_2018.pdf"
    )

    skeleton_page = 151

    page_contents = my_extractor.get_page_contents(skeleton_page)

    return my_extractor.preprocess(
        prompt= """
        Extrae el bloque de estadísticas de un Skeleton.
        """,
        content=page_contents
    )




if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    print(main())


