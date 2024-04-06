from abc import ABC, abstractmethod
from project.campaigns.base_campaign import BaseCampaign

class BaseInfluencer(ABC):
    unique_id = []

    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        # if not value.strip():
        if value.isspace():
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if 0.0 <= value <= 5.0:
            self.__engagement_rate = value
        else:
            raise ValueError("Engagement rate should be between 0 and 5.")
        # if value < 0.0 or value > 5.0:
        #     raise ValueError("Engagement rate should be between 0 and 5.")
        # self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self):
        # if not self.campaigns_participated:
        if len(self.campaigns_participated) == 0:
            return f"{self.username} has not participated in any campaigns."

        # haha = "\n".join(x(f"  - Campaign ID: {x.campaign_id}, Brand: {x.brand}, Reached followers: {self.followers}")
        #                  for x in self.campaigns_participated)
        # return f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:\n" \
        #        f"{haha}"

        result = f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:"

        for campaign in self.campaigns_participated:
            result += "\n" + (f"  - Campaign ID: {campaign.campaign_id}, "
                              f"Brand: {campaign.brand}, "
                              f"Reached followers: {self.reached_followers(type(campaign).__name__)}")

        return result






