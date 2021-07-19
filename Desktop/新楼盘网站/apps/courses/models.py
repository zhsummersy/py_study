from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher
from apps.organizations.models import CourseOrg

from DjangoUeditor.models import UEditorField

"""
实体1 <关系> 实体2
楼房 特点 视频 楼房资源
"""
#2. 实体的具体字段

#3. 每个字段的类型，是否必填


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="房产经纪人")
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name="楼盘信息")
    name = models.CharField(verbose_name="楼房名", max_length=50)
    desc = models.CharField(verbose_name="楼房描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="选购热度(分钟数)")
    degree = models.CharField(verbose_name="类别", choices=(("cj", "商业用地"), ("zj", "综合用地"), ("gj", "住宅用地")), max_length=2)
    students = models.IntegerField(default=0, verbose_name='选购人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    notice = models.CharField(verbose_name="楼房公告", max_length=300, default="")
    category = models.CharField(default=u"房地产开发商", max_length=20, verbose_name="楼房类别")
    tag = models.CharField(default="", verbose_name="楼房标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="楼房须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="经纪人告诉你")
    is_classics = models.BooleanField(default=False, verbose_name="是否热门")
    detail = UEditorField(verbose_name="楼房详情", width=600, height=300, imagePath="courses/ueditor/images/",
                          filePath="courses/ueditor/files/", default="")
    is_banner = models.BooleanField(default=False, verbose_name="是否广告位")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)

    class Meta:
        verbose_name = "楼房信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()

    def show_image(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<img src='{}'>".format(self.image.url))
    show_image.short_description = "图片"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='/course/{}'>跳转</a>".format(self.id))
    go_to.short_description = "跳转"


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播楼房"
        verbose_name_plural = verbose_name
        proxy = True


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="楼房")
    tag = models.CharField(max_length=100, verbose_name="标签")

    class Meta:
        verbose_name = "楼房标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="楼房")  #on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name = models.CharField(max_length=100, verbose_name="特点")
    learn_times = models.IntegerField(default=0, verbose_name="选购热度(分钟数)")

    class Meta:
        verbose_name = "楼房特点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="特点", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"选购热度(分钟数)")
    url = models.CharField(max_length=1000, verbose_name=u"访问地址")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="楼房")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m", verbose_name="下载地址", max_length=200)

    class Meta:
        verbose_name = "楼房资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
