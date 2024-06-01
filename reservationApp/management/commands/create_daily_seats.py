from django.core.management.base import BaseCommand
from django.utils import timezone
from reservationApp.models import Bus, Schedule, Seats

class Command(BaseCommand):
    help = 'Create schedules and seats for daily buses'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        buses = Bus.objects.filter(isDaily=True, status='1')

        for bus in buses:
            try:
                # Fetch the latest schedule for the bus
                latest_schedule = Schedule.objects.filter(bus=bus).latest('schedule')
                
                # Create a new schedule based on the latest one
                new_schedule = Schedule.objects.create(
                    code=latest_schedule.code,
                    bus=bus,
                    depart=latest_schedule.depart,
                    destination=latest_schedule.destination,
                    schedule=latest_schedule.schedule,  # Or any other logic to set the new schedule time
                    fare=latest_schedule.fare,
                    status='1'  # Assuming '1' means active
                )
                
                new_schedule.via.set(latest_schedule.via.all())

                # Create new seats and add to the new schedule
                new_seats = []
                for seat_number in range(1, bus.seats + 1):
                    seat = Seats.objects.create(
                        seat_number=seat_number,
                        is_booked=False
                    )
                    new_seats.append(seat)

                # Add seats to the new schedule
                new_schedule.seats.add(*new_seats)

                self.stdout.write(self.style.SUCCESS(f'Successfully created new schedule and seats for bus {bus.bus_number}'))
            except Schedule.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'No existing schedule found for bus {bus.bus_number}, skipping.'))
