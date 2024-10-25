

from xy_work.Settings.Section.Project import Project as xyProject
class Project(xyProject):
    def get_name(self) -> str | None:
        return "xy_web_project"

from xy_work.Settings.Section.Runner import Runner as xyWorkRunner

class Runner(xyWorkRunner):
    def get_name(self) -> str | None:
        return "xy_web_runner"

from pathlib import Path
from xy_web_settings.Settings import Settings as xySettings

class Settings(xySettings):
    project: Project | None
    runner: Runner | None

    def reload(self, settings_cfg_path: Path):
        super().reload(settings_cfg_path)
        self.project = self.__make_section(Project)
        self.runner = self.__make_section(Runner)


if __name__ == "__main__":
    settings = Settings()
    settings.reload(Path("./xy_web.toml"))
    print(f"project ===> {settings.project}")
    print(f"project.name ===> {settings.project.name}")
    print(f"project.identifier ===> {settings.project.identifier}")