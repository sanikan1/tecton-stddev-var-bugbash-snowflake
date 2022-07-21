from tecton import batch_feature_view, Aggregation
from entities import user
from demo_data import transactions
import datetime


@batch_feature_view(
    sources=[transactions],
    entities=[user],
    mode='snowflake_sql',
    aggregation_interval=datetime.timedelta(1),
    aggregations=[
        Aggregation(column='INT_VALUE', function='variance', time_window=datetime.timedelta(days=1)),
        Aggregation(column='INT_VALUE', function='stddev', time_window=datetime.timedelta(days=1)),
    ],
    online=True,
    feature_start_time=datetime.datetime(2022, 5, 1),
    owner='david@tecton.ai',
    description='User transaction totals over a series of time windows, updated daily.'
)
def user_transaction_metrics(transactions):
    return f'''
        SELECT
            USER_ID,
            INT_VALUE,
            TIMESTAMP
        FROM
            {transactions}
        '''
