from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        self.budget = 5000.0
        super().__init__(campaign_id, brand, required_engagement, self.budget)

    def check_eligibility(self, engagement_rate: float):
        valid = self.required_engagement * 1.20
        if engagement_rate >= valid:
            return True
        return False

