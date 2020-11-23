from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from . import models

class HomePageView(TemplateView):
    template_name = 'index.html'


class TripsView(ListView):
    model = models.Trip
    template_name = 'trips.html'
    context_object_name = 'all_trips_list' # new    

class TripCreateView(CreateView):
    model = models.Trip
    template_name = 'trip_new.html'
    fields = ('name',)
    success_url = reverse_lazy('core:trips')

class TripDeleteView(DeleteView):
    model = models.Trip
    template_name = 'trip_delete.html'
    success_url = reverse_lazy('core:trips')    

class TripEditView(UpdateView):
    model = models.Trip
    points = models.ShowPoint.objects.all()
    trip_points = models.TripPoint.objects.all()
    print(">>>>>>>")
    print(len(trip_points))
    print("<<<<<<<")
    extra_context = {"points":list(points),"trip_points":list(trip_points)}
    template_name = 'trip_edit.html'
    fields = ('name',)
    success_url = reverse_lazy('core:trips')     

class PointsView(ListView):
    model = models.ShowPoint
    template_name = 'points.html'
    context_object_name = 'points_list'

class PointCreateView(CreateView):
    model = models.ShowPoint
    template_name = 'point_new.html'
    fields = ('name','latitude','longitude')
    success_url = reverse_lazy('core:points')

class PointDeleteView(DeleteView):
    model = models.ShowPoint
    template_name = 'point_delete.html'
    success_url = reverse_lazy('core:points')

class PointEditView(UpdateView):
    model = models.ShowPoint
    template_name = 'point_edit.html'
    fields = ('name','latitude','longitude')
    success_url = reverse_lazy('core:points')


class ObjectsView(ListView):
    model = models.ShowObject
    template_name = 'objects.html'
    context_object_name = 'objects_list'

class ObjectCreateView(CreateView):
    model = models.ShowObject
    template_name = 'object_new.html'
    fields = ('name','latitude','longitude')
    success_url = reverse_lazy('core:objects')

class ObjectDeleteView(DeleteView):
    model = models.ShowObject
    template_name = 'object_delete.html'
    success_url = reverse_lazy('core:objects')

class ObjectEditView(UpdateView):
    model = models.ShowObject
    template_name = 'object_edit.html'
    fields = ('name','latitude','longitude')
    success_url = reverse_lazy('core:objects')

class PhotosView(ListView):
    model = models.Photo
    template_name = 'photos.html'
    context_object_name = 'photos_list'

class PhotoCreateView(CreateView):
    model = models.Photo
    template_name = 'photo_new.html'
    fields = '__all__'
    success_url = reverse_lazy('core:photos')

class PhotoDeleteView(DeleteView):
    model = models.Photo
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('core:photos')

class PhotoEditView(UpdateView):
    model = models.Photo
    template_name = 'photo_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('core:photos')

def trip_point_add(request, pk, point_id):
    trip_point = models.TripPoint(
        trip = models.Trip.objects.get(id = pk),
        point = models.ShowPoint.objects.get(id = point_id))
    trip_point.save()
    return HttpResponseRedirect(reverse('core:trip_edit', kwargs={'pk':pk}))

def trip_point_delete(request, pk, point_id):
    trip_point = models.TripPoint.objects.get(
        trip = models.Trip.objects.get(id = pk),
        point = models.ShowPoint.objects.get(id = point_id))
    trip_point.delete()
    return HttpResponseRedirect(reverse('core:trip_edit', kwargs={'pk':pk}))    

def trip_point_up(request, pk, point_id):
    # trip_point = models.TripPoint.objects.filter(
    #     trip = models.Trip.objects.get(id = pk),
    #     point = models.ShowPoint.objects.get(id = point_id))
    # trip_point.delete()
    return HttpResponseRedirect(reverse('core:trip_edit', kwargs={'pk':pk}))      

def trip_point_down(request, pk, point_id):
    # trip_point = models.TripPoint.objects.filter(
    #     trip = models.Trip.objects.get(id = pk),
    #     point = models.ShowPoint.objects.get(id = point_id))
    # trip_point.delete()
    return HttpResponseRedirect(reverse('core:trip_edit', kwargs={'pk':pk}))      
