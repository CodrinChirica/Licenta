from locust import HttpLocust, TaskSet, task


class FiiSite(TaskSet):

    @task(2)
    class Homepage(TaskSet):

        @task
        def task_firstPage(self):
            self.client.get("http://85.122.23.81:8080/xwiki/bin/view/Main/")

        @task
        def stop(self):
            self.interrupt()

    @task(4)
    class Timetable(TaskSet):

        @task
        class Students(TaskSet):

            @task
            def task_students(self):
                self.client.get(
                    "http://profs.info.uaic.ro/~orar/orar_studenti.html")

            @task
            def task_IA5(self):
                self.client.get(
                    "http://profs.info.uaic.ro/~orar/participanti/orar_I1A5.html")

            @task
            def stop(self):
                self.interrupt()

        @task
        class Profs(TaskSet):

            @task
            def task_profs(self):
                self.client.get(
                    "http://profs.info.uaic.ro/~orar/orar_profesori.html")

            @task
            def task_IfteneAdrian(self):
                self.client.get(
                    "http://profs.info.uaic.ro/~orar/participanti/orar_iftene_a.html")

            @task
            def stop(self):
                self.interrupt()


class MyLocust(HttpLocust):
    # http://85.122.23.81:8080/xwiki/bin/view/Main/
    # host = "http://85.122.23.81:8080/xwiki/bin/view/Main/"
    task_set = FiiSite
    min_wait = 1000  # timp de asteptare intre 1 si 5 secunde intre requesturile userilor
    max_wait = 5000
