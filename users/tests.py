from django.test import TestCase
from django.urls import reverse

from .models import User


class RegistrationRoleTests(TestCase):
    def test_reader_can_switch_to_owner_registration(self):
        response = self.client.get(reverse('register_borrower'))

        self.assertContains(
            response,
            reverse('register_owner')
        )
        self.assertContains(response, 'Register as owner')

    def test_owner_can_switch_to_reader_registration(self):
        response = self.client.get(reverse('register_owner'))

        self.assertContains(
            response,
            reverse('register_borrower')
        )
        self.assertContains(response, 'Register as reader')

    def test_owner_registration_assigns_owner_role(self):
        response = self.client.post(
            reverse('register_owner'),
            {
                'username': 'new_owner',
                'role': 'BORROWER',
                'password1': 'StrongRegistrationPass839!',
                'password2': 'StrongRegistrationPass839!',
            }
        )

        self.assertRedirects(response, reverse('owner_dashboard'))
        self.assertEqual(
            User.objects.get(username='new_owner').role,
            'OWNER'
        )

    def test_reader_registration_assigns_borrower_role(self):
        response = self.client.post(
            reverse('register_borrower'),
            {
                'username': 'new_reader',
                'role': 'OWNER',
                'password1': 'StrongRegistrationPass839!',
                'password2': 'StrongRegistrationPass839!',
            }
        )

        self.assertRedirects(response, reverse('all_books'))
        self.assertEqual(
            User.objects.get(username='new_reader').role,
            'BORROWER'
        )
