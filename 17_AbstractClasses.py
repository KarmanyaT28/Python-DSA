return JsonResponse(
    [{'label': name, 'value': name} for name in names],
    safe=False
)
