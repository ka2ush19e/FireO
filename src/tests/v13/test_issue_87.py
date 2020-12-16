from fireo.fields import TextField
from fireo.models import Model


def test_fix_issue_87():
    class CompanyIssue87(Model):
        name = TextField()

    c1 = CompanyIssue87.collection.create(name="Abc_company")
    c2 = CompanyIssue87.collection.create()
    c3 = CompanyIssue87.collection.create()

    assert c1 is not None
    assert c2 is not None
    assert c3 is not None

    c_l = CompanyIssue87.collection.fetch()
    assert len(list(c_l)) == 3
