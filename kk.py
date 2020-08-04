
def get_ric(exchange_dict):
        start = exchange_dict("start")
        end = exchange_dict("end")
        while(start < end):
            yield str(start) + "." + exchange_dict("exchange_name")
            start += 1


