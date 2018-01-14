from django.core.management.base import BaseCommand, CommandError
from manager.models import Class
from manager.models import Schedule
from manager.models import Slot
from manager.models import Room
from manager.models import Requirement

import json



class Command(BaseCommand):

    def load_json_data(self, file_name):
        with open(file_name) as json_data:
            f_json = json.load(json_data)
        return f_json

    def create_json_data(self, file_name, data):
        with open(file_name, 'w') as file:
            file.write(str(data))

    def models_to_file(self, file_name):
        models = {
            "schedules": [],
            "requirements": [],
            "rooms": [],
            "slots": [],
            "classes": []
        }

        schedules = Schedule.get_used_schedules()
        slots = Slot.get_slots_by_schedules(schedules)
        classes = Class.get_scheduled_classes()
        rooms = Room.objects.all()

        for requirement in Requirement.objects.all():
            requirement_model = {
                "id" : requirement.id,
                "type": requirement.type.id,
                "priority": requirement.priority
            }
            models["requirements"].append(requirement_model)

        for schedule in schedules:
            schedules_model = {
                "id": schedule.id,
                "day": schedule.day.id,
                "time_interval": schedule.time_interval.id
            }
            models["schedules"].append(schedules_model)

        for slot in slots:
            slot_model = {
                "id": slot.id,
                "capacity": slot.room.capacity,
                "room": slot.room.id,
                "schedule": Schedule.objects.get(day = slot.day, time_interval = slot.time_interval).id
            }
            models["slots"].append(slot_model)

        for s_class in classes:
            class_model = {
                "id": s_class.id,
                "size": s_class.size,
                "schedules": list(s_class.schedules.all().values_list('id', flat=True)),
                "requirements": list(s_class.requirements.through.objects.all().values_list('id', flat=True))
            }
            models["classes"].append(class_model)

        for room in rooms:
            room_model = {
                "id": room.id,
                "specifications": list(room.specifications.through.objects.all().values_list('id', flat=True)),
                "capacity": room.capacity
            }
            models["rooms"].append(room_model)

        self.create_json_data(file_name, json.dumps(models, indent=4, sort_keys=False))

    def add_arguments(self, parser):
        parser.add_argument('type_request', type=str)
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        type_request = options['type_request']
        file_name = options['file_name']
        print("processing request...")

        if type_request == "request":
            print("creating {0} file...".format(file_name))
            self.models_to_file(file_name)
            print("the file {0} was created...".format(file_name))
            print("request \"{0}\" completed successfully...".format(type_request))

        else:
            print("type request invalid!")
