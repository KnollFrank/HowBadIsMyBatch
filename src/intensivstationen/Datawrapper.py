import requests
import json
import pandas as pd


class Datawrapper:

    def __init__(self, accessToken):
        self.authHeader = {"Authorization": f"Bearer {accessToken}"}

    def setChartTitle(self, title):
        response = requests.request(
            "PATCH",
            "https://api.datawrapper.de/v3/charts/dYmYb",
            json={"title": title},
            headers={
                "Accept": "*/*",
                "Content-Type": "application/json"
            } | self.authHeader)
        return json.loads(response.text)

    def uploadChartData(self, data: pd.DataFrame):
        response = requests.request(
            "PUT",
            "https://api.datawrapper.de/v3/charts/dYmYb/data",
            data=data.to_csv(
                index=False,
                columns=['gemeindeschluessel', 'median_free_beds_in_percent', 'Kreis']).encode("utf-8"),
            headers={
                "Accept": "*/*",
                "Content-Type": "text/csv"
            } | self.authHeader)
        return response.text

    def fetchChartData(self):
        response = requests.request(
            "GET",
            "https://api.datawrapper.de/v3/charts/dYmYb/data",
            headers={
                "Accept": "text/csv"
            } | self.authHeader)

        return response.text

    def publishChart(self):
        response = requests.request(
            "POST",
            "https://api.datawrapper.de/v3/charts/dYmYb/publish",
            headers={
                "Accept": "*/*"
            } | self.authHeader)
        return json.loads(response.text)
