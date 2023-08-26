import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from BarChartDescriptionTables import BarChartDescriptionTables


class BarChartDescriptionTablesTest(unittest.TestCase):

    def test_filterValidJensenShannonDistances(self):
        # Given
        barChartDescriptionTable = TestHelper.createDataFrame(
            columns=['BAR_CHART_DESCRIPTION'],
            data=[
                [
                    {
                        'countries':                        ['Germany', 'Hungary'],
                        'Adverse Reaction Reports guessed': [0,         0],
                        'Adverse Reaction Reports known':   [20,        30],
                        'Jensen-Shannon distance':          np.nan
                    }
                ],
                [
                    {
                        'countries':                        ['Germany'],
                        'Adverse Reaction Reports guessed': [70],
                        'Adverse Reaction Reports known':   [80],
                        'Jensen-Shannon distance':          0.4711
                    }
                ]
            ],
            index=pd.Index(
                [
                    '!D0181',
                    '# 009C01A'
                ],
                name='VAX_LOT'))

        # When
        barChartDescriptionTableResult = BarChartDescriptionTables.filter(
            barChartDescriptionTable,
            BarChartDescriptionTables.isValidJensenShannonDistance)

        # Then
        assert_frame_equal(
            barChartDescriptionTableResult,
            TestHelper.createDataFrame(
                columns=['BAR_CHART_DESCRIPTION'],
                data=[
                    [
                        {
                            'countries':                        ['Germany'],
                            'Adverse Reaction Reports guessed': [70],
                            'Adverse Reaction Reports known':   [80],
                            'Jensen-Shannon distance':          0.4711
                        }
                    ]
                ],
                index=pd.Index(
                    [
                        '# 009C01A',
                    ],
                    name='VAX_LOT')),
            check_dtype=True)

    def test_filterHasMinSizeOfGuessedHistogram_true(self):
        # Given
        barChartDescriptionTable = TestHelper.createDataFrame(
            columns=['BAR_CHART_DESCRIPTION'],
            data=[
                [
                    {
                        'countries':                        ['Germany', 'Hungary'],
                        'Adverse Reaction Reports guessed': [10,        20],
                        'Adverse Reaction Reports known':   [20,        30],
                        'Jensen-Shannon distance':          0.4711
                    }
                ]
            ],
            index=pd.Index(
                [
                    '!D0181'
                ],
                name='VAX_LOT'))

        # When
        barChartDescriptionTableResult = BarChartDescriptionTables.filter(
            barChartDescriptionTable,
            lambda barChartDescription:
                BarChartDescriptionTables.hasMinSizeOfGuessedHistogram(
                    barChartDescription,
                    minSizeOfGuessedHistogram=20))

        # Then
        assert_frame_equal(
            barChartDescriptionTableResult,
            barChartDescriptionTable,
            check_dtype=True)

    def test_filterHasMinSizeOfGuessedHistogram_false(self):
        # Given
        barChartDescriptionTable = TestHelper.createDataFrame(
            columns=['BAR_CHART_DESCRIPTION'],
            data=[
                [
                    {
                        'countries':                        ['Germany', 'Hungary'],
                        'Adverse Reaction Reports guessed': [10,        20],
                        'Adverse Reaction Reports known':   [20,        30],
                        'Jensen-Shannon distance':          0.4711
                    }
                ]
            ],
            index=pd.Index(
                [
                    '!D0181'
                ],
                name='VAX_LOT'))

        # When
        barChartDescriptionTableResult = BarChartDescriptionTables.filter(
            barChartDescriptionTable,
            lambda barChartDescription:
                BarChartDescriptionTables.hasMinSizeOfGuessedHistogram(
                    barChartDescription,
                    minSizeOfGuessedHistogram=31))

        # Then
        assert_frame_equal(
            barChartDescriptionTableResult,
            TestHelper.createDataFrame(
                columns=['BAR_CHART_DESCRIPTION'],
                data=[],
                index=pd.Index(
                    [],
                    name='VAX_LOT')),
            check_dtype=True)

    def test_filterHasCountryWithGuessedGreaterThanKnown(self):
        # Given
        guessed = 25
        known = 20
        barChartDescriptionTable = TestHelper.createDataFrame(
            columns=['BAR_CHART_DESCRIPTION'],
            data=[
                [
                    {
                        'countries':                        ['Germany', 'Hungary'],
                        'Adverse Reaction Reports guessed': [guessed,   20],
                        'Adverse Reaction Reports known':   [known,     30],
                        'Jensen-Shannon distance':          0.4711
                    }
                ],
                [
                    {
                        'countries':                        ['Germany', 'America'],
                        'Adverse Reaction Reports guessed': [25,        20],
                        'Adverse Reaction Reports known':   [250,       200],
                        'Jensen-Shannon distance':          0.815
                    }
                ]],
            index=pd.Index(
                [
                    '!D0181',
                    'some batch code'
                ],
                name='VAX_LOT'))

        # When
        barChartDescriptionTableResult = BarChartDescriptionTables.filter(
            barChartDescriptionTable,
            BarChartDescriptionTables.hasCountryWithGuessedGreaterThanKnown)

        # Then
        assert_frame_equal(
            barChartDescriptionTableResult,
            TestHelper.createDataFrame(
                columns=['BAR_CHART_DESCRIPTION'],
                data=[
                    [
                        {
                            'countries':                        ['Germany', 'Hungary'],
                            'Adverse Reaction Reports guessed': [guessed,   20],
                            'Adverse Reaction Reports known':   [known,     30],
                            'Jensen-Shannon distance':          0.4711
                        }
                    ]
                ],
                index=pd.Index(
                    [
                        '!D0181'
                    ],
                    name='VAX_LOT')),
            check_dtype=True)
