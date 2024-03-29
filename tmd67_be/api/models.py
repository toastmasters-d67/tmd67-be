from django.db import models


class Agency(models.Model):
    level = models.CharField(max_length=8)
    division = models.CharField(max_length=3)
    area = models.IntegerField(blank=True, null=True)


class Role(models.Model):
    en_title = models.CharField(max_length=255, blank=True, null=True)
    tw_title = models.CharField(max_length=255)


class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    chinese_name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    achievement = models.CharField(max_length=50, blank=True, null=True)
    member_no = models.CharField(max_length=20, blank=True, null=True)
    line = models.CharField(max_length=20, blank=True, null=True)


class Club(models.Model):
    agency = models.ForeignKey(Agency, models.CASCADE)
    club_number = models.IntegerField()
    chinese_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    charter_date = models.DateField(blank=True, null=True)
    meeting_week = models.CharField(max_length=255, blank=True, null=True)
    meeting_day = models.CharField(max_length=9, blank=True, null=True)
    meeting_start = models.TimeField(blank=True, null=True)
    meeting_end = models.TimeField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255)
    club_type = models.CharField(max_length=9)
    qualification = models.CharField(max_length=8, blank=True, null=True)
    fee = models.CharField(max_length=255, blank=True, null=True)
    abbr = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    en_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)


class Event(models.Model):
    tw_title = models.CharField(max_length=250)
    en_title = models.CharField(max_length=250, blank=True, null=True)
    member = models.ForeignKey(Member, models.CASCADE)
    contents = models.TextField(blank=True, null=True)
    agenda = models.TextField(blank=True, null=True)
    countdown = models.DateField()
    deadline = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    address = models.CharField(max_length=250, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    vacancy = models.IntegerField()
    standby = models.IntegerField()
    target = models.CharField(max_length=250, blank=True, null=True)
    fee = models.CharField(max_length=150)
    languages = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    cover_photo = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    memo = models.CharField(max_length=250, blank=True, null=True)


class Attachment(models.Model):
    event = models.ForeignKey(Event, models.CASCADE)
    name = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)


class Office(models.Model):
    member = models.ForeignKey(Member, models.CASCADE)
    agency = models.ForeignKey(Agency, models.CASCADE)
    club = models.ForeignKey(Club, models.CASCADE, blank=True, null=True)
    role = models.ForeignKey(Role, models.CASCADE)
    print = models.IntegerField(blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    confirm = models.IntegerField(blank=True, null=True)


class Path(models.Model):
    en_name = models.CharField(max_length=255)
    tw_name = models.CharField(max_length=255)
    show_name = models.CharField(max_length=255)
    initialism = models.CharField(max_length=2)
    en_description = models.TextField()
    tw_description = models.TextField()

    class Meta:
        unique_together = (("en_name",),)

    def __str__(self):
        return f"Path(id={self.id}, en_name={self.en_name}"


class Project(models.Model):
    en_name = models.CharField(max_length=255)
    tw_name = models.CharField(max_length=255, null=True)
    show_name = models.CharField(max_length=255)
    en_description = models.TextField(null=True)
    tw_description = models.TextField(null=True)
    en_purpose = models.TextField(null=True)
    tw_purpose = models.TextField(null=True)
    en_overview = models.TextField(null=True)
    tw_overview = models.TextField(null=True)
    en_includes = models.JSONField(null=True)
    tw_includes = models.JSONField(null=True)
    en_form = models.JSONField(null=True)
    tw_form = models.JSONField(null=True)

    class Meta:
        unique_together = (("en_name",),)


class ProjectInclude(models.Model):
    en_name = models.CharField(max_length=255, null=True)
    tw_name = models.CharField(max_length=255, null=True)
    en_form = models.FileField(upload_to="en_form/", null=True)
    tw_form = models.FileField(upload_to="tw_form/", null=True)
    project = models.ForeignKey(
        Project, models.CASCADE, related_name="includes"
    )


class Level(models.Model):
    level = models.IntegerField()
    en_name = models.CharField(max_length=255)
    tw_name = models.CharField(max_length=255)
    is_elective = models.BooleanField()
    elective_number = models.IntegerField()
    is_old = models.BooleanField()
    path = models.ForeignKey(Path, models.CASCADE, related_name="levels")
    project = models.ForeignKey(Project, models.CASCADE, related_name="levels")
