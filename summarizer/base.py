from abc import ABC, abstractmethod

class BaseSummarizer(ABC):

    @abstractmethod
    def summarize(self, text: str, summary_type: str):
        pass
