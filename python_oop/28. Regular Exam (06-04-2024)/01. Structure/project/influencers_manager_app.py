from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class InfluencerManagerApp:
    valid_influencers = []
    valid_campaigns = []

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []


    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type != "StandardInfluencer" or "PremiumInfluencer":
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        influencer = self.valid_influencers[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        pass

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        pass

    def calculate_total_reached_followers(self):
        pass

    def influencer_campaign_report(self, username: str):
        pass

    def campaign_statistics(self):
        pass




