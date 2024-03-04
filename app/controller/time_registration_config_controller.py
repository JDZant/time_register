from ..model.time_registration_config import TimeRegistrationConfig


class TimeRegistrationConfigController:
    @staticmethod
    def get_time_registration_config_by_id(config_id):
        return TimeRegistrationConfig.get_by_id(config_id)

    @classmethod
    def get_all_time_registration_configs(cls):
        return TimeRegistrationConfig.get_all()
