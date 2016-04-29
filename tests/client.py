import json

import requests

from tests.config import cfg
from tests.log import log_response


class BaseClient(object):

    @classmethod
    def get(cls):
        return cls(cfg.CONF.api.base_url)

    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def url(self, *args):
        parts = [self.base_url]
        parts.extend([str(x).lstrip('/') for x in args])
        return '/'.join(parts)


class ProjectClientMixin(BaseClient):

    @log_response
    def list_projects(self, params=None):
        return requests.get(self.url('/projects'), params=params)

    @log_response
    def create_project(self, data, params=None):
        url = self.url('/projects')
        return requests.post(url, data=json.dumps(data), params=params)


class SuiteClientMixin(BaseClient):

    @log_response
    def list_suites(self, project_id, params=None):
        url = self.url(project_id, '/suites')
        return requests.get(url, params=params)

    @log_response
    def create_suite(self, project_id, data, params=None):
        url = self.url(project_id, '/suites')
        return requests.post(url, data=json.dumps(data), params=params)

    @log_response
    def get_suite(self, project_id, suite_id, params=None):
        url = self.url(project_id, '/suites', suite_id)
        return requests.get(url, params=params)

    @log_response
    def delete_suite(self, project_id, suite_id, params=None):
        url = self.url(project_id, '/suites', suite_id)
        return requests.delete(url, params=params)


class BuildClientMixin(BaseClient):

    @log_response
    def list_builds(self, project_id, suite_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds')
        return requests.get(url, params=params)

    @log_response
    def create_build(self, project_id, suite_id, data, params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds')
        return requests.post(url, data=json.dumps(data), params=params)

    @log_response
    def get_build(self, project_id, suite_id, build_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds', build_id)
        return requests.get(url, params=params)

    @log_response
    def delete_build(self, project_id, suite_id, build_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds', build_id)
        return requests.delete(url, params=params)


class SuiteResultClientMixin(BaseClient):

    @log_response
    def list_suite_results(self, project_id, suite_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/results')
        return requests.get(url, params=params)

    @log_response
    def create_suite_result(self, project_id, suite_id, data, params=None):
        url = self.url(project_id, '/suites', suite_id, '/results')
        return requests.post(url, data=json.dumps(data), params=params)

    @log_response
    def get_suite_result(self, project_id, suite_id, result_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/results', result_id)
        return requests.get(url, params=params)

    @log_response
    def delete_suite_result(self, project_id, suite_id, result_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/results', result_id)
        return requests.delete(url, params=params)


class BuildResultClientMixin(BaseClient):

    @log_response
    def list_build_results(self, project_id, suite_id, build_id, params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds', build_id,
                       '/results')
        return requests.get(url, params=params)

    @log_response
    def create_build_result(self, project_id, suite_id, build_id, data,
                            params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds', build_id,
                       '/results')
        return requests.post(url, data=json.dumps(data), params=params)

    @log_response
    def get_build_result(self, project_id, suite_id, build_id, result_id,
                         params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds', build_id,
                       '/results', result_id)
        return requests.get(url, params=params)

    @log_response
    def delete_build_result(self, project_id, suite_id, build_id, result_id,
                            params=None):
        url = self.url(project_id, '/suites', suite_id, '/builds', build_id,
                       '/results', result_id)
        return requests.delete(url, params=params)


class TetraClient(
    ProjectClientMixin,
    SuiteClientMixin,
    BuildClientMixin,
    SuiteResultClientMixin,
    BuildResultClientMixin,
):
    pass
