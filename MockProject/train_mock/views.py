from flask import request
from utils import *
from flask_restful import Resource
from train_mock.serializers import *

class Train(Resource):

    def get(self):

        args = TrainSerializer().parse_args()
        fromStation = args.get('fromStation')
        toStation = args.get('toStation')
        trainDate = args.get('trainDate')

        # print(args)
        fromStationCode = pinyin(fromStation)
        toStationCode = pinyin(toStation)
        data = {"queryKey":"123456","fromStation":fromStation,"fromStationCode":fromStationCode,"toStation":toStation,"toStationCode":toStationCode,"trainDate":trainDate,"pageIndex":0,"pageSize":0,"totalCount":1,"totalSize":0,"trains":[{"serialNumber":1,"trainNo":"K777","fromTime":"23:36","toTime":"07:32","fromStation":fromStation,"fromStationCode":fromStationCode,"toStation":toStation,"toStationCode":toStationCode,"runTimeSpan":"476","fromPassType":1,"toPassType":1,"bookState":1,"trainClass":"KS","note":"","tickets":{"noseat":{"seatName":"无座","price":78.0,"seatState":0,"seats":"0","upPrice":0.0,"midPrice":0.0,"downPrice":0.0,"waitBuyFlag":"0"},"hardsleepermid":{"seatName":"硬卧","price":148.0,"seatState":0,"seats":"0","upPrice":139.0,"midPrice":144.0,"downPrice":148.0,"waitBuyFlag":"1"},"hardseat":{"seatName":"硬座","price":78.0,"seatState":1,"seats":"21","upPrice":0.0,"midPrice":0.0,"downPrice":0.0,"waitBuyFlag":"1"}},"miles":0,"pullInByIdCard":1,"saleFlag":"0","saleDateTime":"","payByPoint":"0","trainLongNo":"55000K8356G2","waitBuyFlag":"1","smartFlag":"0"}],"froms":[{"station":fromStation,"location":""}],"tos":[{"station":toStation,"location":""}],"canNotBookEndTime":"","FromInterval":0,"ToInterval":0,"msgCode":"100","msgInfo":"请求成功"}

        return data

class TrainNo(Resource):

    def get(self):

        args = TrainNoSerializer().parse_args()
        trainNo = args.get('trainNo')
        trainDate = args.get('trainDate')


        data = {"msgCode":"100", "msgInfo":"查询成功", "trainNo":trainNo, "trainClass":"GD", "fromStation":"北京南", "fromStationCode":"beijingnan", "fromStationNo":"53", "departureTime":"07:00", "toStation":"上海虹桥", "toStationCode":"shanghaihongqiao", "toStationNo":"321", "trainDate":trainDate, "arrivalTime":"12:37", "miles":1318, "runTimeSpan":337, "prices":"一等座 933.0 无座 553.0 二等座 553.0 商务座 1748.0 ", "stations":[{"serialNumber":1, "trainNo":"G101","fromStation":"北京南","fromStationCode":"beijingnan","fromStationNo":"53", "departureTime":"07:02", "arrivalTime":"07:00", "stayTimeSpan":0, "runTimeSpan":0, "miles":0}], "seats":[{"seatType":1, "seatPrice":100.00,"ticketCount":30,"bookState":2}]}

        return data



class IdentityVerification(Resource):

    def get(self):


        data = {"msgCode":"100","msgInfo":"请求成功","passengers":[{"passengerType":"1","cardType":"1","cardNo":"123456789","passengerName":"小王","status":"succeed","encMobileNo":"17788889999","captcha":None,"mobileStatus":"succeed"}]}

        return data


class BookTickets(Resource):

    def post(self):

        args = BookTicketsSerializer().parse_args()
        outOrderNo = args.get('outOrderNo')

        orderNO = train_orderNO(22)
        data ={"msgCode":"100","msgInfo":"请求成功","orderNo":orderNO,"outOrderNo":outOrderNo,"data":None}

        return data



class applyIssueOrder(Resource):

    def get(self):

        args = applyIssueOrderSerializer().parse_args()
        orderNo = args.get('orderNo')

        data = {"msgCode":"100","msgInfo":"请求成功","orderNo":orderNo,"data":None}

        return data


class orderDetail(Resource):

    def get(self):

        args = orderDetailSerializer().parse_args()
        orderNo = args.get('orderNo')
        outOrderNo = args.get('outOrderNo')
        data = {"msgCode":"100", "msgInfo":"订单查询成功","orderNo":orderNo,"outOrderNo":outOrderNo,"orderState":"占座失败","orderStateCode":"B","failureReason":"乘客身份信息核验未通过","bookTime":"2014-11-20 11:32:27","payTime":"2014-11-20 11:32:27","issueTime":"2014-11-20 11:32:27","placeTime":"2016-05-17 11:27:27","payType":"微信钱包","payStatus":"-1","payInfo":"余额不足","orderPrice":"100.00","serviceFeeTotal":"10","postFeeAmount":"1","ticketNo":"E123456","changeFee":"1.00","trainNo":"6801","trainDate":"2014-11-21","fromStation":"太原","toStation":"太原东","departureTime":"2014-11-21 06:30:00","arrivalTime":"2014-11-21 06:35:00","passengers":[{"passengerId":"2966769","passengerName":"张三","passengerType":"1","idType":"1","idCard":"XXXXXXXXXX","birthday":"1988-02-10","seatClass":"firstseat","seatClassName":"一等座","seatNo":"10车厢，12A","pTicketNo":"E123456789","ticketStateCode":"N","ticketState":"未出票","ticketPrice":100.00,"insureUnitPrice":20,"insureState":"F","insureBillNo":"XXXXXX","refundFee":"2.00","refundTime":"2017-06-25 12:35:12","ticketGate":"检票口26"}],"contactInfo":{"person":"张三","cellphone":"13000000000","email":""}}

        return data
