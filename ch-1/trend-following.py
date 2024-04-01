current_position = 0
PROFIT_EXIT_PRICE_PERCENT =0.2
LOSS_EXIT_PRICE_PERCENT = -0.1


def SendSellOrderAtCurrentPrice():
    return {'message': "Successful placed a sell order"}

def SendBuyOrderAtCurrentPrice():
    return {'message': "Successful placed a buy order"}

def OnMarketPriceChange(current_price, current_time):
    if current_position == 0 and (current_price - price_two_hours_ago)/ current_price > 0.1:
        SendBuyOrderAtCurrentPrice()
        current_position += 1

    elif current_position == 0 and (current_price - price_two_hours_ago) / current_price < -0.1:
        SendSellOrderAtCurrentPrice()
        current_position -= 1
    
    if current_position > 0 and (current_price - position_price) > PROFIT_EXIT_PRICE_PERCENT:
        SendSellOrderAtCurrentPrice()
        current_position -= 1

    elif current_position > 0 and (current_price - position_price) < LOSS_EXIT_PRICE_PERCENT:
        SendSellOrderAtCurrentPrice()
        current_position -= 1
    elif current_position < 0 and (position_price - current_price) > PROFIT_EXIT_PRICE_PERCENT:
        SendBuyOrderAtCurrentPrice()
        current_position -= 1
    elif current_position < 0 and (position_price - current_price) < LOSS_EXIT_PRICE_PERCENT:
        SendBuyOrderAtCurrentPrice()
        current_position -= 1
