import copy


class Car:
    def __init__(self, m, t, e):
        self.model = m
        self.tires = t
        self.engine = e

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj

    def get_objects(self):
        return self._objects


car_1 = Car('model_1', 'tires_1', 'engine_1')
car_2 = Car('model_2', 'tires_2', 'engine_2')

proto = Prototype()

proto.register_object('car_1', car_1)
proto.register_object('car_2', car_2)
print(proto.get_objects())

car_3 = proto.clone('car_2')
print(car_3)

car_4 = proto.clone('car_2', model='model_4', tires='tires_4', engine='engine_4')
print(car_4)

