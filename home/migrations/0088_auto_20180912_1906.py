# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-12 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0087_priorfossexperience_prior_contrib_self_identify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierstoparticipation',
            name='barriers_to_contribution',
            field=models.TextField(help_text="Please provide specific examples. Outreachy organizers strongly encourage you to write your personal stories. We want you to know that we won't judge your writing style, grammar or spelling.", verbose_name='What barriers or concerns have kept you from contributing to free and open source software?'),
        ),
        migrations.AlterField(
            model_name='barrierstoparticipation',
            name='systematic_bias',
            field=models.TextField(help_text="<p>Contributing to free and open source software takes some skill. You may have already learned some basic skills through university or college classes, specialized schools, online classes, online resources, or with a mentor, friend, family member or co-worker.</p><p>In these settings, have you faced systematic bias or discrimination? Have you been discouraged from accessing these resources because of your identity or background?</p><p>Please provide specific examples and (optionally) statistics. Outreachy Organizers strongly encourage you to write your personal stories. We want you to know that we won't judge your writing style, grammar or spelling.</p>", verbose_name='What systematic bias or discrimination have you faced while building your skills for contributing to free and open source software?'),
        ),
        migrations.AlterField(
            model_name='priorfossexperience',
            name='prior_contributor',
            field=models.BooleanField(help_text='<p>Outreachy welcomes applicants who are newcomers to free and open source software (FOSS). We also welcome applicants who have made contributions to FOSS, and want to take the next step in their FOSS career. Outreachy asks this questions to see if we are meeting our goal of promoting free software to people from groups under-represented in the technology industry.</p><p>Please exclude contributions that were made as part of a prior Outreachy application period.</p>', verbose_name='Have you contributed to free and open source software before?'),
        ),
    ]