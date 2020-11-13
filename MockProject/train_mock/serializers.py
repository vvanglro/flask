import decimal

from flask_restful import reqparse
from werkzeug.datastructures import FileStorage


class Argument(reqparse.Argument):
    """
    继承自 reqparse.Argument, 重写源码的convert方法
    对于值为 '' 并且 nullable=False 的字段 raise TypeError
    """
    def convert(self, value, op):
        # if value is '' and not self.nullable:
        #     raise ValueError('Must not be null!')
        # return super(Argument, self).convert(value, op)

        # Don't cast None
        if value is '' or value is None:
            if self.nullable:
                return None
            else:
                raise ValueError('Must not be null!')

        # and check if we're expecting a filestorage and haven't overridden `type`
        # (required because the below instantiation isn't valid for FileStorage)
        elif isinstance(value, FileStorage) and self.type == FileStorage:
            return value

        try:
            return self.type(value, self.name, op)
        except TypeError:
            try:
                if self.type is decimal.Decimal:
                    return self.type(str(value))
                else:
                    return self.type(value, self.name)
            except TypeError:
                return self.type(value)

def TrainSerializer():
    # 1.创建解析器对象
    parser = reqparse.RequestParser(argument_class=Argument)

    # 2.利用解析器对象添加 需要验证的参数
    parser.add_argument('fromStation', type=str, help='出发城市！', required=True, trim=True, nullable=False)
    parser.add_argument('toStation', type=str, help='到达城市！', required=True, trim=True, nullable=False)
    parser.add_argument('trainDate', type=str, help='日期！', required=True, trim=True, nullable=False)

    return parser


def TrainNoSerializer():
    # 1.创建解析器对象
    parser = reqparse.RequestParser(argument_class=Argument)

    # 2.利用解析器对象添加 需要验证的参数
    parser.add_argument('trainNo', type=str, help='车次号！', required=True, trim=True,nullable=False)
    parser.add_argument('trainDate', type=str, help='发车日期！', required=True, trim=True , nullable=False)

    return parser

def BookTicketsSerializer():
    # 1.创建解析器对象
    parser = reqparse.RequestParser(argument_class=Argument)

    # 2.利用解析器对象添加 需要验证的参数
    parser.add_argument('outOrderNo', type=str, help='外部订单号！', required=True, trim=True, nullable=False)

    return parser


def applyIssueOrderSerializer():
    # 1.创建解析器对象
    parser = reqparse.RequestParser(argument_class=Argument)

    # 2.利用解析器对象添加 需要验证的参数
    parser.add_argument('orderNo', type=str, help='订单号！', required=True, trim=True, nullable=False)

    return parser

def orderDetailSerializer():
    # 1.创建解析器对象
    parser = reqparse.RequestParser(argument_class=Argument)

    # 2.利用解析器对象添加 需要验证的参数
    parser.add_argument('orderNo', type=str, help='订单号！', required=True, trim=True, nullable=False)
    parser.add_argument('outOrderNo', type=str, help='外部订单号！', required=True, trim=True, nullable=False)

    return parser