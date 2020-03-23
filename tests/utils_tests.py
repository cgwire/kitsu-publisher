
from gazupublisher.views.TasksTab import TasksTab
import unittest.mock
class MockResponse:
    @staticmethod
    def tasks():
        return [{'assignees': ['4a4603a0-72a3-455a-8da0-aaa100d6cbd8'], 'id': 'e71d0286-cfff-4651-bc64-680caa91c382',
                    'created_at': '2020-03-10T14:32:12', 'updated_at': '2020-03-11T14:04:42', 'name': 'main',
                    'description': None, 'priority': 0, 'duration': 0, 'estimation': 0, 'completion_rate': 0,
                    'retake_count': 0, 'sort_order': 0, 'start_date': None, 'end_date': None, 'due_date': None,
                    'real_start_date': None, 'last_comment_date': '2020-03-11T14:04:42', 'data': None,
                    'shotgun_id': None,
                    'project_id': '5061f75f-ddaf-4877-8889-d85dae4c1297',
                    'task_type_id': 'd196d341-61d2-4382-ab2d-9582fd72f8f0',
                    'task_status_id': 'a78b28d7-0f89-422a-94f6-dc3f8a0d5a8d',
                    'entity_id': '31b0cf98-2c97-4c71-b8f4-972318926d55',
                    'assigner_id': '4a4603a0-72a3-455a-8da0-aaa100d6cbd8', 'type': 'Task', 'project_name': 'Test',
                    'project_has_avatar': False, 'entity_name': 'Env3', 'entity_description': 'Un bel environnement',
                    'entity_preview_file_id': '', 'entity_source_id': '', 'entity_type_name': 'Environment',
                    'sequence_name': None, 'episode_id': '', 'episode_name': None, 'task_estimation': 0,
                    'task_duration': 0,
                    'task_due_date': None, 'task_type_name': 'Concept', 'task_status_name': 'Todo',
                    'task_type_color': '#8D6E63', 'task_status_color': '#f5f5f5', 'task_status_short_name': 'todo',
                    'last_comment': {'text': 'cc', 'date': '2020-03-11T14:04:42',
                                     'person_id': '4a4603a0-72a3-455a-8da0-aaa100d6cbd8'}},
                   {'assignees': ['4a4603a0-72a3-455a-8da0-aaa100d6cbd8'], 'id': '4034af63-9a26-42d4-87e2-e86d1446a584',
                    'created_at': '2020-03-10T11:13:14', 'updated_at': '2020-03-11T13:59:55', 'name': 'main',
                    'description': None, 'priority': 0, 'duration': 0, 'estimation': 0, 'completion_rate': 0,
                    'retake_count': 0, 'sort_order': 0, 'start_date': None, 'end_date': None, 'due_date': None,
                    'real_start_date': None, 'last_comment_date': '2020-03-11T13:59:55', 'data': None,
                    'shotgun_id': None,
                    'project_id': '5061f75f-ddaf-4877-8889-d85dae4c1297',
                    'task_type_id': '00a7d10e-6d15-44da-8c28-67514990d949',
                    'task_status_id': 'a78b28d7-0f89-422a-94f6-dc3f8a0d5a8d',
                    'entity_id': '000a470a-2143-4f94-8a84-438b3bd436c0',
                    'assigner_id': '4a4603a0-72a3-455a-8da0-aaa100d6cbd8', 'type': 'Task', 'project_name': 'Test',
                    'project_has_avatar': False, 'entity_name': 'Char1', 'entity_description': 'Ceci est un perso',
                    'entity_preview_file_id': '', 'entity_source_id': '', 'entity_type_name': 'Characters',
                    'sequence_name': None, 'episode_id': '', 'episode_name': None, 'task_estimation': 0,
                    'task_duration': 0,
                    'task_due_date': None, 'task_type_name': 'Modeling', 'task_status_name': 'Todo',
                    'task_type_color': '#78909C', 'task_status_color': '#f5f5f5', 'task_status_short_name': 'todo',
                    'last_comment': {'text': 'quelle belle modé !', 'date': '2020-03-11T13:59:55',
                                     'person_id': '4a4603a0-72a3-455a-8da0-aaa100d6cbd8'}}]

    @staticmethod
    def connection():
        return [{'id': '4a4603a0-72a3-455a-8da0-aaa100d6cbd8', 'created_at': '2020-03-04T21:44:09',
                 'updated_at': '2020-03-04T21:44:09', 'first_name': 'Random', 'last_name': 'Admin',
                 'email': 'random@example.com', 'phone': '', 'active': True, 'last_presence': None,
                 'desktop_login': '', 'shotgun_id': None, 'timezone': 'Europe/Paris', 'locale': 'en_US',
                 'data': None, 'role': 'admin', 'has_avatar': False, 'notifications_enabled': False,
                 'notifications_slack_enabled': False, 'notifications_slack_userid': '', 'type': 'Person',
                 'full_name': 'Random'}]

    @staticmethod
    def tab_columns():
        return {"entity_name": "Nom", "task_type_name": "Type de tâche",
                "created_at": "Date de création", "last_comment": "Commentaire",
                "task_status_name": "Task status"}

    @staticmethod
    def status_names():
        return [{'id': 'd4292814-70a7-4fab-be05-19c26e54cb83', 'created_at': '2020-03-04T21:43:59',
                 'updated_at': '2020-03-04T21:43:59', 'name': 'Done', 'short_name': 'done', 'color': '#22d160',
                 'is_done': True, 'is_artist_allowed': True, 'is_client_allowed': True, 'is_retake': False,
                 'shotgun_id': None, 'is_reviewable': True, 'type': 'TaskStatus'},
                {'id': '208c2a97-04af-4bad-8ad5-3f1e34ad1242', 'created_at': '2020-03-04T21:43:59',
                 'updated_at': '2020-03-04T21:43:59', 'name': 'Retake', 'short_name': 'retake', 'color': '#ff3860',
                 'is_done': False, 'is_artist_allowed': True, 'is_client_allowed': True, 'is_retake': True,
                 'shotgun_id': None, 'is_reviewable': True, 'type': 'TaskStatus'},
                {'id': 'a78b28d7-0f89-422a-94f6-dc3f8a0d5a8d', 'created_at': '2020-03-04T21:43:59',
                 'updated_at': '2020-03-04T21:43:59', 'name': 'Todo', 'short_name': 'todo', 'color': '#f5f5f5',
                 'is_done': False, 'is_artist_allowed': True, 'is_client_allowed': True, 'is_retake': False,
                 'shotgun_id': None, 'is_reviewable': True, 'type': 'TaskStatus'},
                {'id': '5d6b74d3-df9a-4307-b45c-d73af1d14816', 'created_at': '2020-03-04T21:43:59',
                 'updated_at': '2020-03-04T21:43:59', 'name': 'Waiting For Approval', 'short_name': 'wfa',
                 'color': '#ab26ff', 'is_done': False, 'is_artist_allowed': True, 'is_client_allowed': True,
                 'is_retake': False, 'shotgun_id': None, 'is_reviewable': True, 'type': 'TaskStatus'},
                {'id': 'e909e0ee-5a93-49f7-be76-0818a077ed9c', 'created_at': '2020-03-04T21:43:59',
                 'updated_at': '2020-03-04T21:43:59', 'name': 'Work In Progress', 'short_name': 'wip',
                 'color': '#3273dc', 'is_done': False, 'is_artist_allowed': True, 'is_client_allowed': True,
                 'is_retake': False, 'shotgun_id': None, 'is_reviewable': True, 'type': 'TaskStatus'}]