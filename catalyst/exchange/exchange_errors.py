from catalyst.errors import ZiplineError


class ExchangeRequestError(ZiplineError):
    msg = (
        'Request failed: {error}'
    ).strip()


class ExchangeRequestErrorTooManyAttempts(ZiplineError):
    msg = (
        'Request failed: {error}, giving up after {attempts} attempts'
    ).strip()


class ExchangeBarDataError(ZiplineError):
    msg = (
        'Unable to retrieve bar data: {data_type}, ' +
        'giving up after {attempts} attempts: {error}'
    ).strip()


class ExchangePortfolioDataError(ZiplineError):
    msg = (
        'Unable to retrieve portfolio data: {data_type}, ' +
        'giving up after {attempts} attempts: {error}'
    ).strip()


class ExchangeTransactionError(ZiplineError):
    msg = (
        'Unable to execute transaction: {transaction_type}, ' +
        'giving up after {attempts} attempts: {error}'
    ).strip()


class ExchangeAuthNotFound(ZiplineError):
    msg = (
        'Please create an auth.json file containing the api token and key for '
        'exchange {exchange}. Place the file here: {filename}'
    ).strip()


class ExchangeSymbolsNotFound(ZiplineError):
    msg = (
        'Unable to download or find a local copy of symbols.json for exchange '
        '{exchange}. The file should be here: {filename}'
    ).strip()


class InvalidHistoryFrequencyError(ZiplineError):
    msg = (
        'History frequency {frequency} not supported by the exchange.'
    ).strip()