from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        self.budget = 2500.0
        super().__init__(campaign_id, brand, required_engagement, self.budget)


    def check_eligibility(self, engagement_rate: float):
        valid = self.required_engagement * 0.90
        if engagement_rate >= valid:
            return True
        return False