from flask import Flask  # include the flask library 
app = Flask(__name__) 
from py_zipkin import Encoding #import Zipkin package 
from py_zipkin.zipkin import zipkin_span #import Zipkin package 
from transport import http_transport #import Zipkin transport 
import requests, time

@zipkin_span(service_name='storefront', span_name='service1-storefront')
def service1():
    time.sleep(2)
    service2()

@zipkin_span(service_name='catalogue', span_name='service2-catalogue')
def service2():
    time.sleep(5)
    
@zipkin_span(service_name='orders', span_name='service3-orders')
def service3():
    service4()

@zipkin_span(service_name='payment', span_name='service4-payment')
def service4():
    pass
# http://127.0.0.1:5000/tracing
@app.route("/tracing") 
def apm_tracing():

    with zipkin_span(  
        service_name="DemoAPMApp", #You can change it as you need
        span_name="Demo OCI APM App Spans", #You can change it as you need
        transport_handler=http_transport, #zipkin transport, will use it to upload trace data to OCI APM
        encoding = Encoding.V2_JSON,
        binary_annotations = {"oci-apm":"This is a Test APM tracing web application"}, #Custom tag
        sample_rate=100 # this is optional and can be used to set custom sample rates
    ):
        service1()
        service3()
    return 'This is a Test APM tracing web application'
if __name__ == '__main__': 
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000