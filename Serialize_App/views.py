
from django.http import HttpResponse
import  json
from Serialize_App.models import Employee

from django.views import View
from django.core.serializers import serialize
from Serialize_App.mixins import is_json
from Serialize_App.forms import EmployeeForm

from Serialize_App.mixins import SerializeMixin


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListView(SerializeMixin, View):
    def get(self,request):
        emps = Employee.objects.all()
        json_meta_data = serialize('json',emps)

        json_data = self.user_defined_serailze(json_meta_data)
        # p_data = json.loads(json_data)
        #
        # emp_list = []
        #
        # for obj in p_data:
        #     emp = obj['fields']
        #     emp_list.append(emp)
        #
        # json_data = json.dumps(emp_list)
        return HttpResponse(json_data, content_type='application/json', status=200)


    def post(self,request):
        data = request.body
        valid_json = is_json(data)

        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid JSON type data'})
            return HttpResponse(json_data['msg'],content_type='application/json',status=400)

        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Data created successfully'})
            return HttpResponse(json_data, content_type='application/json', status=201)

        else:
            json_data = json.dumps({'msg': 'Data not created successfully'})
            return HttpResponse(json_data, content_type='application/json', status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailView(SerializeMixin,View):

    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp


    def get(self,request,pk):
        try:
            emp = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            json_data = {'msg': 'Record not available'}
            return HttpResponse(json_data['msg'], content_type='application/json', status=404)
        else:
            json_meta_data = serialize('json',[emp])
            json_data = self.user_defined_serailze(json_meta_data)

            # p_data = json.loads(json_data)
            #
            # emp_list = []
            #
            # for obj in p_data:
            #     emp = obj['fields']
            #     emp_list.append(emp)
            #
            # json_data = json.dumps(emp_list)

            return HttpResponse(json_data, content_type='application/json', status=200)


    def put(self,request,pk):
        emp = self.get_object_by_id(pk)

        if emp is None:
            json_data = {'msg': 'Record not available for updating'}
            return HttpResponse(json_data['msg'], content_type='application/json', status=404)

        data = request.body
        valid_json = is_json(data)

        if not  valid_json:
            json_data = {'msg': 'Please send valid JSON type data'}
            return HttpResponse(json_data, content_type='application/json', status=400)

        provided_data = json.loads(data)

        original_data = {
            'ename' : emp.ename,
            'esal' : emp.esal,
            'eaddr' : emp.eaddr,
        }

        original_data.update(provided_data)

        form = EmployeeForm(original_data, instance=emp)

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Data updated successfully'})
            return HttpResponse(json_data, content_type='application/json', status=200)
        else:
            json_data = json.dumps({'msg': 'Data not updated successfully'})
            return HttpResponse(json_data, content_type='application/json', status=400)



    def delete(self,request,pk):
        emp = self.get_object_by_id(pk)

        if emp is None:
            json_data = {'msg': 'Record not available for deleting'}
            return HttpResponse(json_data, content_type='application/json', status=404)

        emp.delete()
        json_data = {'msg': 'Record deleting successfully'}
        return HttpResponse(json_data, content_type='application/json', status=204)































