from django.shortcuts import render


def test_page_view(request):
    return render(request, 'test/test.html')