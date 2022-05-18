import json
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from django.forms.models import model_to_dict

from common.search import get_search_result
from mainapp.models import SaveSearch

logger = logging.getLogger(__name__)


def query_survey():
    save_search = SaveSearch.objects.all()

    for item in save_search:
        params = {}
        params['adults'] = str(item.adults)
        params['children'] = str(item.children)
        params['infants'] = str(item.infants)
        params['travelClass'] = item.travelClass
        params['nonStop'] = item.nonStop.lower()
        params['destinationLocationCode'] = item.destinationLocationCode
        params['originLocationCode'] = item.originLocationCode
        params['departureDate'] = item.departureDate.strftime("%Y-%m-%d")
        if item.returnDate:
            params['returnDate'] = item.returnDate.strftime("%Y-%m-%d")
        params['currencyCode'] = item.currencyCode

        json_res = get_search_result(params)
        json_data = json_res['data']
        route = json.loads(item.route)

        # данные полученный из API
        for data in json_data:
            # данные itineraries полученный из API
            for itinerarie in data['itineraries']:
                # данные взятые из БД route
                for item_route in route:
                    # Проверка времени полета
                    if (item_route['duration'] == itinerarie['duration']):
                        # Смотрим пересадки из БД
                        for flight in item_route['flights']:
                            # Смотрим пересадки из API
                            for segment in itinerarie['segments']:
                                if (
                                        segment['departure']['iataCode'] ==
                                        flight['departure']['iataCode'] and
                                        segment['departure']['at'] ==
                                        flight['departure']['at'] and
                                        segment['arrival']['iataCode'] ==
                                        flight['arrival']['iataCode'] and
                                        segment['arrival']['at'] ==
                                        flight['arrival']['at']
                                ):
                                    # Проверяем цену!
                                    if (float(data['price']['total']) != float(item.total)):
                                        print(f"Цена изменилась! Старая {item.total}. Новая {data['price']['total']}")
                                    else:
                                        print('Ok')
                                else:
                                    # если пересадка не совпала выходим
                                    break
                    else:
                        # если время полета не совпало, выходим
                        break


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            query_survey,
            trigger=CronTrigger(second="*/15"),
            id="synchronization_with_ldap",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
