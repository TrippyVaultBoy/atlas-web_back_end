import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        """

        expected = {"login": org_name, "id": 123}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """
        """

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"
            }
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        """

        expected = [{"name": "repo1", "private": False},
                    {"name": "repo2", "private": False},
                    {"name": "repo3", "private": False},
                    {"name": "repo4", "private": False},
                    {"name": "repo5", "private": False},]
        
        mock_get_json.return_value = expected

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_url:

            mock_url.return_value = "https://mock.url"
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            expected_repos = [repo["name"] for repo in expected]

            self.assertEqual(result, expected_repos)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://mock.url")