from drug_database.cli import app
from typer.testing import CliRunner

runner = CliRunner(mix_stderr=False)


def test_list_drugs():
    result = runner.invoke(app, ["list-drugs"])
    assert result.exit_code == 0
    assert "Dofetilide" in result.output


def test_list_drug_with_fpc():
    result = runner.invoke(app, ["show-drug-with-fpc", "verapamil", "1"])
    assert result.exit_code == 0
    assert "Verapamil and FPC 1" in result.output
    assert "scale_drug_INa" in result.output
