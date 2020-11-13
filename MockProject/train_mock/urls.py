from flask import Blueprint
from train_mock.views import *
from flask_restful import Api

train_bp = Blueprint('train', __name__)
train = Api(train_bp)
train.add_resource(Train,'/wh/TrainSearch/train')
train.add_resource(TrainNo,'/wh/trainsearch/TrainNo')
train.add_resource(IdentityVerification,'/wh/trainOrder/IdentityVerification')
train.add_resource(BookTickets,'/wh/trainOrder/bookTickets')
train.add_resource(applyIssueOrder,'/wh/trainOrder/applyIssueOrder')
train.add_resource(orderDetail,'/wh/trainOrder/orderDetail')


