# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import enum
from typing import Any, List, Optional, Sequence, Tuple, overload

from tensorflow.compiler.xla.python import xla_extension

ChannelHandle = xla_extension.ChannelHandle
FftType = xla_extension.FftType
XlaBuilder = xla_extension.XlaBuilder
XlaComputation = xla_extension.XlaComputation
XlaOp = xla_extension.XlaOp
PrecisionConfig_Precision = xla_extension.PrecisionConfig_Precision
PrimitiveType = xla_extension.PrimitiveType
Shape = xla_extension.Shape
ShapeIndex = xla_extension.ShapeIndex

_ConvDimensionNumbers = Any
_DotDimensionNumbers = Any
_Layout = Any
_LiteralSlice = Any
_GatherDimensionNumbers = Any
_PaddingConfig = Any
_ReplicaGroup = Any
_ScatterDimensionNumbers = Any

class TriangularSolveOptions_Transpose(enum.IntEnum):
  TRANSPOSE_INVALID: int
  NO_TRANSPOSE: int
  TRANSPOSE: int
  ADJOINT: int

class RandomAlgorithm(enum.IntEnum):
  RNG_DEFAULT: int
  RNG_THREE_FRY: int
  RNG_PHILOX: int

class CustomCallSchedule(enum.IntEnum):
  SCHEDULE_NONE: int
  SCHEDULE_LATEST: int
  SCHEDULE_EARLIEST: int

# TODO(b/189822916): Remove this enum when all clients are migrated to the
# status-returning API.
class CustomCallApiVersion(enum.IntEnum):
  API_VERSION_ORIGINAL: int
  API_VERSION_STATUS_RETURNING: int

def AfterAll(builder: XlaBuilder, tokens: Sequence[XlaOp]) -> XlaOp: ...
def AllGather(
    operand: XlaOp,
    all_gather_dimension: int,
    shard_count: int,
    replica_groups: Sequence[_ReplicaGroup] = ...,
    channel_id: Optional[ChannelHandle] = ...,
    shape_with_layout: Optional[_Layout] = ...,
    use_global_device_placement: Optional[bool] = ...) -> XlaOp: ...
def AllReduce(
    operand: XlaOp,
    computation: XlaComputation,
    replica_groups: Sequence[_ReplicaGroup] = ...,
    channel_id: Optional[ChannelHandle] = ...,
    shape_with_layout: Optional[_Layout] = ...) -> XlaOp: ...
def ApproxTopK(
    builder: XlaBuilder,
    operands: Sequence[XlaOp],
    init_values: Sequence[XlaOp],
    top_k: int,
    reduction_dim: int,
    comparator: XlaComputation,
    recall_target: Optional[float],
    aggregate_to_topk: Optional[bool],
    reduction_input_size_override: Optional[int]) -> XlaOp: ...
def ApproxTopKReductionOutputSize(
    input_size: int,
    rank: int,
    top_k: int,
    recall_target: float,
    aggregate_to_topk: Optional[bool] = ...,
    input_size_override: Optional[int] = ...) -> Tuple[int, int]: ...
def ReduceScatter(
    operand: XlaOp,
    computation: XlaComputation,
    scatter_dimension: int,
    shard_count: int,
    replica_groups: Sequence[_ReplicaGroup] = ...,
    channel_id: Optional[ChannelHandle] = ...,
    layout: Optional[_Layout] = ...,
    use_global_device_ids: Optional[bool] = ...) -> XlaOp: ...
def AllToAll(
    operand: XlaOp,
    split_dimension: int,
    concat_dimension: int,
    split_count: int,
    replica_groups: Sequence[_ReplicaGroup] = ...,
    layout: Optional[_Layout] = ...) -> XlaOp: ...
def BitcastConvertType(operand: XlaOp,
                       new_element_type: PrimitiveType) -> XlaOp: ...
def Broadcast(operand: XlaOp, sizes: Sequence[int]) -> XlaOp: ...
def BroadcastInDim(operand: XlaOp,
                   shape: Sequence[int],
                   broadcast_dimensions: Sequence[int]) -> XlaOp: ...
def Call(builder: XlaBuilder,
         computation: XlaComputation,
         operands: Sequence[XlaOp]) -> XlaOp: ...
def Cholesky(a: XlaOp, lower: bool = ...) -> XlaOp: ...
def Clamp(min: XlaOp, operand: XlaOp, max: XlaOp) -> XlaOp: ...
def Collapse(operand: XlaOp, dimensions: Sequence[int]) -> XlaOp: ...
def CollectivePermute(
  operand: XlaOp,
    source_target_pairs: Sequence[Tuple[int, int]]) -> XlaOp: ...
def ConcatInDim(builder: XlaBuilder,
                operands: Sequence[XlaOp],
                dimension: int) -> XlaOp: ...
@overload
def Conditional(branch_index: XlaOp,
                branch_computations: Sequence[XlaComputation],
                branch_operands: Sequence[XlaOp]) -> XlaOp: ...
@overload
def Conditional(
  predicate: XlaOp,
    true_operand: XlaOp,
    true_computation: XlaComputation,
    false_operand: XlaOp,
    false_computation: XlaComputation) -> XlaOp: ...

def Constant(builder: XlaBuilder, value: _LiteralSlice) -> XlaOp: ...
def ConstantLiteral(builder: XlaBuilder, value: _LiteralSlice) -> XlaOp: ...
def ConvGeneralDilated(
    lhs: XlaOp,
    rhs: XlaOp,
    window_strides: Sequence[int],
    padding: Sequence[Tuple[int, int]],
    lhs_dilation: Sequence[int],
    rhs_dilation: Sequence[int],
    dimension_numbers: _ConvDimensionNumbers,
    feature_group_count: int = ...,
    batch_group_count: int = ...,
    precision_config: PrecisionConfig_Precision = ...,
    preferred_element_type: Optional[PrimitiveType] = ...) -> XlaOp: ...
def ConvertElementType(
    operand: XlaOp,
    new_element_type: PrimitiveType) -> XlaOp: ...
def CreateToken(builder: XlaBuilder) -> XlaOp: ...
def CrossReplicaSum(
    operand: XlaOp,
    replica_groups: Sequence[_ReplicaGroup] = ...) -> XlaOp: ...
def CustomCall(
    builder: XlaBuilder,
    call_target_name: bytes,
    operands: Sequence[XlaOp],
    shape: Shape,
    opaque: bytes = ...,
    has_side_effect: bool = ...,
    schedule: CustomCallSchedule = ...,
    api_version: CustomCallApiVersion = ...) -> XlaOp: ...
def CustomCallWithLayout(
    builder: XlaBuilder,
    call_target_name: bytes,
    operands: Sequence[XlaOp],
    shape_with_layout: Shape,
    operand_shapes_with_layout: Sequence[Shape],
    opaque: bytes = ...,
    has_side_effect: bool = ...,
    schedule: CustomCallSchedule = ...,
    api_version: CustomCallApiVersion = ...) -> XlaOp: ...
def CustomCallWithAliasing(
    builder: XlaBuilder,
    call_target_name: bytes,
    operands: Sequence[XlaOp],
    shape_with_layout: Shape,
    operand_shapes_with_layout: Sequence[Shape],
    opaque: bytes = ...,
    has_side_effect: bool = ...,
    output_operand_aliasing: Sequence[Tuple[ShapeIndex, Tuple[int, ShapeIndex]]] = ...,
    literal: _LiteralSlice = ...,
    schedule: CustomCallSchedule = ...,
    api_version: CustomCallApiVersion = ...) -> XlaOp: ...
def Dot(
    lhs: XlaOp,
    rhs: XlaOp,
    precision_config: PrecisionConfig_Precision = ...,
    preferred_element_type: Optional[PrimitiveType] = ...) -> XlaOp: ...
def DotGeneral(
    lhs: XlaOp,
    rhs: XlaOp,
    dimensions_numbers: _DotDimensionNumbers,
    precision_config: PrecisionConfig_Precision = ...,
    preferred_element_type: Optional[PrimitiveType] = ...) -> XlaOp: ...
def DynamicReshape(
    operand: XlaOp,
    dim_sizes: Sequence[XlaOp],
    new_size_bounds: Sequence[int],
    dims_are_dynamic: Sequence[bool]) -> XlaOp: ...
def DynamicSlice(
    operand: XlaOp,
    start_indices: Sequence[XlaOp],
    slice_sizes: Sequence[int]) -> XlaOp: ...
def DynamicUpdateSlice(
    operand: XlaOp,
    update: XlaOp,
    start_indices: Sequence[XlaOp]) -> XlaOp: ...
def Eigh(
    a: XlaOp,
    lower: bool = ...,
    max_iter: int = ...,
    epsilon: float = ...,
    sort_eigenvalues: bool = ...) -> Tuple[XlaOp, XlaOp]: ...
def Fft(
    operand: XlaOp,
    fft_type: FftType,
    fft_length: Sequence[int]) -> XlaOp: ...
def Gather(
    a: XlaOp,
    start_indices: XlaOp,
    dimension_numbers: _GatherDimensionNumbers,
    slice_sizes: Sequence[int],
    indices_are_sorted: bool = ...) -> XlaOp: ...
def GetDimensionSize(operand: XlaOp, index: int) -> XlaOp: ...
def GetTupleElement(tuple_data: XlaOp, index: int) -> XlaOp: ...
def InfeedWithToken(
    token: XlaOp,
    shape: Shape,
    config: Optional[str] = ...) -> XlaOp: ...
@overload
def Iota(builder: XlaBuilder, shape: Shape, iota_dimension: int) -> XlaOp: ...
@overload
def Iota(builder: XlaBuilder, type: PrimitiveType, size: int) -> XlaOp: ...
def LU(a: XlaOp) -> Tuple[XlaOp, XlaOp, XlaOp]: ...
def Map(
    builder: XlaBuilder,
    operands: Sequence[XlaOp],
    computation: XlaComputation,
    dimensions: Sequence[int],
    static_operands: Sequence[XlaOp] = ...) -> XlaOp: ...
def NextAfter(__from: XlaOp, to: XlaOp) -> XlaOp: ...
def OutfeedWithToken(
    operand: XlaOp,
    token: XlaOp,
    shape_with_layout: Shape,
    outfeed_config: Optional[str] = ...) -> XlaOp: ...
def Pad(
    operand: XlaOp,
    padding_value: XlaOp,
    padding_config: _PaddingConfig) -> XlaOp: ...
def Parameter(
    builder: XlaBuilder,
    parameter_number: int,
    shape: Shape,
    name: str = ...,
    replicated_at_leaf_buffers: Sequence[bool] = ...) -> XlaOp: ...
def QR(a: XlaOp, full_matrices: bool) -> Tuple[XlaOp, XlaOp]: ...
def Reduce(
    builder: XlaBuilder,
    operands: Sequence[XlaOp],
    init_values: Sequence[XlaOp],
    computation: XlaComputation,
    dimensions_to_reduce: Sequence[int]) -> XlaOp: ...
def ReducePrecision(
    operand: XlaOp,
    exponent_bits: int,
    mantissa_bits: int) -> XlaOp: ...
@overload
def ReduceWindowWithGeneralPadding(
    operand: XlaOp,
    init_value: XlaOp,
    computation: XlaComputation,
    window_dimensions: Sequence[int],
    window_strides: Sequence[int],
    base_dilations: Sequence[int],
    window_dilations: Sequence[int],
    padding: Sequence[Tuple[int, int]]) -> XlaOp: ...
@overload
def ReduceWindowWithGeneralPadding(
    operands: Sequence[XlaOp],
    init_values: Sequence[XlaOp],
    computation: XlaComputation,
    window_dimensions: Sequence[int],
    window_strides: Sequence[int],
    base_dilations: Sequence[int],
    window_dilations: Sequence[int],
    padding: Sequence[Tuple[int, int]]) -> XlaOp: ...
def ReplicaId(builder: XlaBuilder) -> XlaOp: ...
@overload
def Reshape(
    operand: XlaOp,
    dimensions: Sequence[int],
    new_sizes: Sequence[int]) -> XlaOp: ...
@overload
def Reshape(operand: XlaOp, new_sizes: Sequence[int]) -> XlaOp: ...
def Rev(operand: XlaOp, dimensions: Sequence[int]) -> XlaOp: ...
def RngBitGenerator(
    algorithm: RandomAlgorithm,
    initial_state: XlaOp,
    shape: Shape) -> XlaOp: ...
def RngNormal(mu: XlaOp, sigma: XlaOp, shape: Shape) -> XlaOp: ...
def RngUniform(a: XlaOp, b: XlaOp, shape: Shape) -> XlaOp: ...
def Scatter(
    input: XlaOp,
    scatter_indices: XlaOp,
    updates: XlaOp,
    update_computation: XlaComputation,
    dimension_numbers: _ScatterDimensionNumbers,
    indices_are_sorted: bool = ...,
    unique_indices: bool = ...) -> XlaOp: ...
def Select(pred: XlaOp, on_true: XlaOp, on_false: XlaOp) -> XlaOp: ...
def SelectAndScatterWithGeneralPadding(
    operand: XlaOp,
    select: XlaComputation,
    window_dimensions: Sequence[int],
    window_strides: Sequence[int],
    padding: Sequence[Tuple[int, int]],
    source: XlaOp,
    init_value: XlaOp,
    scatter: XlaComputation) -> XlaOp: ...
def Slice(
    operand: XlaOp,
    start_indices: Sequence[int],
    limit_indices: Sequence[int],
    strides: Sequence[int]) -> XlaOp: ...
def SliceInDim(
    operand: XlaOp,
    start_index: int,
    limit_index: int,
    stride: int,
    dimno: int) -> XlaOp: ...
def Sort(
    builder: XlaBuilder,
    operands: Sequence[XlaOp],
    comparator: Optional[XlaComputation] = ...,
    dimension: int = ...,
    is_stable: bool = ...) -> XlaOp: ...
def SVD(
    a: XlaOp,
    max_iter: int = ...,
    epsilon: float = ...) -> Tuple[XlaOp, XlaOp, XlaOp]: ...
def TopK(input: XlaOp, k: int) -> XlaOp: ...
def Transpose(operand: XlaOp, permutation: Sequence[int]) -> XlaOp: ...
def TriangularSolve(
    a: XlaOp,
    b: XlaOp,
    left_side: bool,
    lower: bool,
    unit_diagonal: bool,
    transpose_a: TriangularSolveOptions_Transpose) -> XlaOp: ...
def Tuple(builder: XlaBuilder, elements: Sequence[XlaOp]) -> XlaOp: ...
def While(
    condition: XlaComputation,
    body: XlaComputation,
    init: XlaOp) -> XlaOp: ...


def Igamma(a: XlaOp, x: XlaOp) -> XlaOp: ...
def Igammac(a: XlaOp, x: XlaOp) -> XlaOp: ...
def IgammaGradA(a: XlaOp, x: XlaOp) -> XlaOp: ...
def RandomGammaGrad(a: XlaOp, x: XlaOp) -> XlaOp: ...
def RegularizedIncompleteBeta(a: XlaOp, b: XlaOp, x: XlaOp) -> XlaOp: ...
def Zeta(a: XlaOp, q: XlaOp) -> XlaOp: ...

def Eq(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Ne(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Ge(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Gt(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Lt(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Le(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Add(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Sub(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Mul(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Div(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Rem(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Max(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Min(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def And(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Or(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Xor(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def ShiftLeft(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def ShiftRightArithmetic(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def ShiftRightLogical(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Atan2(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Pow(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...
def Complex(lhs: XlaOp, rhs: XlaOp, broadcast_dimensions: Sequence[int] = ...) -> XlaOp: ...

def Not(__arg: XlaOp) -> XlaOp: ...
def PopulationCount(__arg: XlaOp) -> XlaOp: ...
def Clz(__arg: XlaOp) -> XlaOp: ...
def Abs(__arg: XlaOp) -> XlaOp: ...
def Exp(__arg: XlaOp) -> XlaOp: ...
def Expm1(__arg: XlaOp) -> XlaOp: ...
def Floor(__arg: XlaOp) -> XlaOp: ...
def Ceil(__arg: XlaOp) -> XlaOp: ...
def Round(__arg: XlaOp) -> XlaOp: ...
def Log(__arg: XlaOp) -> XlaOp: ...
def Log1p(__arg: XlaOp) -> XlaOp: ...
def Sign(__arg: XlaOp) -> XlaOp: ...
def Cos(__arg: XlaOp) -> XlaOp: ...
def Sin(__arg: XlaOp) -> XlaOp: ...
def Tanh(__arg: XlaOp) -> XlaOp: ...
def IsFinite(__arg: XlaOp) -> XlaOp: ...
def Neg(__arg: XlaOp) -> XlaOp: ...
def Sqrt(__arg: XlaOp) -> XlaOp: ...
def Rsqrt(__arg: XlaOp) -> XlaOp: ...
def Cbrt(__arg: XlaOp) -> XlaOp: ...
def Square(__arg: XlaOp) -> XlaOp: ...
def Reciprocal(__arg: XlaOp) -> XlaOp: ...
def Erfc(__arg: XlaOp) -> XlaOp: ...
def Erf(__arg: XlaOp) -> XlaOp: ...
def ErfInv(__arg: XlaOp) -> XlaOp: ...
def Lgamma(__arg: XlaOp) -> XlaOp: ...
def Digamma(__arg: XlaOp) -> XlaOp: ...
def BesselI0e(__arg: XlaOp) -> XlaOp: ...
def BesselI1e(__arg: XlaOp) -> XlaOp: ...
def Acos(__arg: XlaOp) -> XlaOp: ...
def Asin(__arg: XlaOp) -> XlaOp: ...
def Atan(__arg: XlaOp) -> XlaOp: ...
def Tan(__arg: XlaOp) -> XlaOp: ...
def Acosh(__arg: XlaOp) -> XlaOp: ...
def Asinh(__arg: XlaOp) -> XlaOp: ...
def Atanh(__arg: XlaOp) -> XlaOp: ...
def Cosh(__arg: XlaOp) -> XlaOp: ...
def Sinh(__arg: XlaOp) -> XlaOp: ...
def Real(__arg: XlaOp) -> XlaOp: ...
def Imag(__arg: XlaOp) -> XlaOp: ...
def Conj(__arg: XlaOp) -> XlaOp: ...
